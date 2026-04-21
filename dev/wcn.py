import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin


def main() -> None:
    # Read known consoles from wcn.md.
    known = {}
    with Path("dev/wcn.md").open() as f:
        md = f.read()
    begin_mark = "<!-- BEGIN LIST -->\n\n"
    end_mark = "\n<!-- END LIST -->\n"
    begin_index = md.find(begin_mark) + len(begin_mark)
    end_index = md.find(end_mark)
    md_list = md[begin_index:end_index]
    for line in md_list.splitlines():
        if line.startswith("* "):
            parts = line.split(" ", 2)
            console = parts[1]
            remark = (parts[2][1:-1]) if len(parts) == 3 else None
            known[console] = remark
    # Read crawl.json.
    with Path("crawl.json").open() as f:
        data = json.load(f)
    # Write wcn.json.
    data = clean_data(known, data)
    with Path("dev/web/wcn.json").open("w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    # Read wcn.html template.
    with Path("dev/wcn.tmpl.html").open() as f:
        html = f.read()
    # Write wcn.html output.
    out = make_html(html, data)
    with Path("dev/web/wcn.html").open("w") as f:
        f.write(out)
    # Write missing entries.
    out = update_known_list(known, data)
    with Path("dev/wcn.md").open("w") as f:
        f.write(out)


def clean_data(known: dict[str, str], data: dict[str, Any]) -> dict[str, Any]:
    dt = datetime.strptime(data["date"], "%Y-%m-%d %H:%M:%S %z")
    dt = dt.astimezone(timezone.utc)
    data["date"] = dt.strftime("%Y-%m-%d %H:%M:%S %z")
    data["consoles"] = {
        url: value
        for url, value in data["consoles"].items()
        if not url.startswith("file:") and value["visited"]
    }
    for url, value in data["consoles"].items():
        if url in known and known[url]:
            data["consoles"][url]["remark"] = known[url]
        del value["depth"]
        del value["id"]
        del value["visited"]
        value["referrers"] = [
            r for r in value["referrers"] if not r.startswith("file:")
        ]
    for value in data["pages"].values():
        del value["depth"]
        del value["id"]
    return data


def make_html(html: str, data: dict[str, Any]) -> str:
    parts = data["date"].split(" ")
    date = parts[0] + " at " + parts[1] + " UTC"
    consoles = "".join(make_console_html(k, v) for k, v in data["consoles"].items())
    pages = "".join(make_page_html(k, v) for k, v in data["pages"].items())
    out = html.replace("@date", date)
    out = out.replace("@console-count", str(len(data["consoles"])))
    out = out.replace("@page-count", str(len(data["pages"])))
    out = out.replace("@console-list", consoles)
    return out.replace("@page-list", pages)


def make_console_html(url: str, value: dict[str, Any]) -> str:
    remark = value.get("remark")
    note = (" (" + remark + ")") if remark else ""
    out = ""
    out += "      <details>\n"
    out += "        <summary>" + make_console_link(url) + note + "</summary>\n"
    out += "        <p>Found " + count_word(len(value["referrers"]), "console") + " "
    out += " linking to this console:\n"
    out += "        <ul>\n"
    for referrer in value["referrers"]:
        out += "          <li>" + make_console_link(referrer) + "</li>\n"
    out += "        </ul>\n"
    out += "      </details>\n"
    return out


def make_page_html(url: str, value: dict[str, Any]) -> str:
    out = ""
    out += "      <details>\n"
    out += "        <summary>" + make_page_link(url) + "</summary>\n"
    out += "        <p>Found " + count_word(len(value["referrers"]), "console") + " "
    out += " linking to this page:\n"
    out += "        <ul>\n"
    for referrer in value["referrers"]:
        out += "          <li>" + make_console_link(referrer) + "</li>\n"
    out += "        </ul>\n"
    out += "      </details>\n"
    return out


def make_console_link(url: str) -> str:
    js_url = urljoin(url, "wander.js")
    svg = '<svg><use href="#ext-icon"></use></svg>'
    return f'<a href="{url}">{url}{svg}</a> (<a href="{js_url}">JS{svg}</a>)'


def make_page_link(url: str) -> str:
    svg = '<svg><use href="#ext-icon"></use></svg>'
    return f'<a href="{url}">{url}{svg}</a>'


def count_word(count: int, word: str) -> str:
    if count != 1:
        word += "s"
    return f"{count} {word}"


def update_known_list(known: dict[str, str], data: dict[str, Any]) -> None:
    # Remove consoles that occur in the known list but not in crawl data.
    stage = {url: remark for url, remark in known.items() if url in data["consoles"]}
    # Add consoles that occur in crawl data but missing from the known list.
    for key in data["consoles"]:
        if key not in stage:
            stage[key] = None
    # Update known file.
    with Path("dev/wcn.md").open() as f:
        md = f.read()
    begin_mark = "<!-- BEGIN LIST -->\n\n"
    end_mark = "\n<!-- END LIST -->\n"
    begin_index = md.find(begin_mark) + len(begin_mark)
    end_index = md.find(end_mark)
    out = md[:begin_index]
    out = re.sub(r"contains \d+ known", f"contains {len(stage)} known", out)
    for url, remark in stage.items():
        extra = (" (" + remark + ")") if remark else ""
        out += f"* {url}{extra}\n"
    out += md[end_index:]
    return out


if __name__ == "__main__":
    main()
