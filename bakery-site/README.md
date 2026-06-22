# Zuurdesem — Sourdough Bakery (Tilburg)

A single-page website with a 3D parallax hero for a sourdough bakery in Tilburg.

## What's inside
- **3D parallax hero** — layered scene that reacts to mouse movement (and device tilt on
  mobile) for depth, plus scroll-driven parallax. Built with CSS `perspective` /
  `transform-style: preserve-3d` and a small vanilla-JS driver.
- **Tilt-on-hover bread cards** — each loaf card tilts in 3D toward the cursor.
- **Scroll reveals & animated counters** — content fades up as it enters the viewport.
- **No build step, no dependencies** — plain HTML/CSS/JS. Only external resource is
  Google Fonts (Fraunces + Inter).
- **Accessible** — honours `prefers-reduced-motion`, semantic landmarks, keyboard-navigable.

## Run it
Just open `index.html` in a browser, or serve the folder:

```bash
cd bakery-site
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Files
```
bakery-site/
├── index.html      # markup & content
├── css/styles.css  # styling, parallax scene, palette
└── js/main.js      # parallax, tilt, reveals, counters
```

## Customising
- **Text / menu / prices** — edit `index.html`.
- **Colours** — the palette lives in the `:root` block at the top of `css/styles.css`.
- **Photos** — the loaf is a hand-built SVG and the menu uses emoji so the site ships with
  zero image assets. Swap in real photography by replacing the `.bread-card__art` blocks
  and the hero `loaf-art` SVG when you have shots of your bakes.

Placeholder details (address, phone, KvK, opening hours) are invented — update them with
your real bakery information before going live.
