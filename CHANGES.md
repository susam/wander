Changelog
=========

0.4.0 (UNRELEASED)
------------------

### Added

- Add asterisk (`*`) wildcard support to ignore patterns

### Changed

- Include the base console in the discovered consoles list, allowing
  it to be selected by the random picker during wandering.

### Fixed

- Fix issue that prevented links with `target="_blank"` from opening.


0.3.0 (2026-03-25)
------------------

### Changed

- Decrease the console history size from 1000 to 100.

### Fixed

- Prevent dialog from overflowing the screen width due to long URLs.
- Allow websites relying on same-origin context to load successfully.
- Prevent recently recommended pages from reappearing too
  soon. (contributed by [4thguy](https://codeberg.org/4thguy)).
- Fix issue where the **Console** dialog box failed to open if the
  `ignore` property was missing from `wander.js`.


0.2.0 (2026-03-24)
------------------

### Added

- Add `styles` property to `wander.js` to support adding custom CSS.
- Add `scripts` property to `wander.js` to support adding custom JavaScript.
- Add `ignore` property to `wander.js` to support ignoring specific URLs.
- Show version number in the **About** dialog.
- Add an **Open** button to open a website recommendation in a new tab.
- Add console screens in the **Console* dialog: Base, Neighbours,
  Pages, Ignores, History, Discovery.

### Changed

- Download link has been updated from
  <https://codeberg.org/susam/wander/archive/main.zip> to
  <https://codeberg.org/susam/wander/archive/wander.zip>.
- If a console presents no pages, its page list is ignored.
- Pick a random console from the most recently discovered 1000
  consoles.  Previously, only neighbours of the most recently visited
  console were considered.
- Title bar and the about dialog now contain the name 'Wander Console'
  rather than just 'Wander'.
- Use kebab-case names for all HTML element IDs and class names.
- Links in dialog boxes open in new tabs.

### Removed

- Replace **Copy** button with **Open** button.

### Security

- Execute `wander.js` of remote consoles in a sandbox.  This prevents
  a remote `wander.js` from running with the same origin as your
  website.  As a result, it cannot access cookies, local storage or
  session storage set by your website.  This also prevents a remote
  `wander.js` from altering your console's user interface, state or
  behaviour.
- Add sandbox settings to the `<iframe>` that loads recommended web
  pages (contributed by [exurd](https://codeberg.org/exurd)).


0.1.0 (2026-03-19)
------------------

### Added

- Create Wander console with six buttons: Wander, Console, Reload, Go,
  Copy, About.
