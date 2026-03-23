Changelog
=========

0.2.0 (UNRELEASED)
------------------

### Added

- Add `styles` property to `wander.js` to support adding custom CSS.
- Add `scripts` property to `wander.js` to support adding custom JavaScript.
- Add `ignore` property to `wander.js` to support ignoring specific URLs.
- Show version number in the **About** dialog.
- Add an **Open** button to open a website recommendation in a new tab.
- Display current host console in the **Console** dialog.

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


0.1.0 (2025-03-19)
------------------

### Added

- Create Wander console with six buttons: Wander, Console, Reload, Go,
  Copy, About.
