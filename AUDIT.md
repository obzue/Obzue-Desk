# WebSim paste audit

## Structural

- Three languages were concatenated. Browsers cannot run that as one document.
- PNG icons and wallpaper were referenced and absent. Desk v0.1 uses CSS/SVG chrome.
- Control Panel and Trash were unregistered. They ship in desktop/os.js.

## Runtime

- Duplicate video element ids, wrong Video.js volume API, Howler never unloaded.
- Local variable `window` shadowed the global.
- Google-in-iframe home fails X-Frame-Options.

## Product claims

- A web desktop cannot take over host PCs or iOS.
