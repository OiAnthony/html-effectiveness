# Repository Guidelines

## Project Structure

```
skills/html-effectiveness/
├── SKILL.md                  # Skill definition and prompt
├── assets/
│   ├── components.css        # Shared semantic component classes
│   └── templates/            # HTML artifact templates
│       ├── changelog.html
│       ├── code-review.html
│       ├── deck.html
│       ├── editor.html
│       ├── exploration.html
│       ├── report.html
│       └── research.html
├── scripts/
│   ├── init.py               # CLI to scaffold artifacts from templates
│   └── shared.py             # Constants, template registry, helpers
└── references/               # Design and category reference docs (gitignored)
```

## Development Commands

```bash
# List available templates
python skills/html-effectiveness/scripts/init.py --list

# Scaffold an artifact
python skills/html-effectiveness/scripts/init.py exploration "API Design Options"
python skills/html-effectiveness/scripts/init.py report --title "Q1 Status" --eyebrow "Engineering"
python skills/html-effectiveness/scripts/init.py deck -t "Pitch Deck" -s "Series A" -o ./deck.html
```

## Coding Conventions

- **HTML templates**: Self-contained single files — inline CSS (Tailwind) and JS, no external dependencies.
- **Python scripts**: Use `from __future__ import annotations`, type hints, and `pathlib.Path` for all file operations.
- **Template placeholders**: Use `{{PLACEHOLDER}}` syntax (e.g. `{{TITLE}}`, `{{SUBTITLE}}`, `{{EYEBROW}}`).
- **New templates**: Register in `TEMPLATE_REGISTRY` in `shared.py` and place the `.html` file in `assets/templates/`.
- **CSS components**: Shared styles go in `assets/components.css`; injected via `inject_components_css()` at the `</style></head>` marker.

## Template Authoring Rules

- Every template must be a complete, valid HTML document that opens directly in a browser.
- No external CDN links, no `<script src="...">`, no `<link rel="stylesheet" href="...">` — everything inline.
- Match the user's language for all visible text content; keep code identifiers in English.

## Commit Guidelines

- Use conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`, `chore:`.
- Keep commits atomic — one logical change per commit.
