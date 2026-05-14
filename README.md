# html-effectiveness

<p align="center"><a href="README.zh-CN.md">简体中文</a></p>

A hobby project inspired by [ThariqS/html-effectiveness](https://github.com/ThariqS/html-effectiveness) — after reading that article I wanted an agent skill that actually does it.

Make your AI agent output self-contained HTML files instead of Markdown. Comparisons, code reviews, status reports, slide decks — HTML gives you higher information density and is easier to read.

Once installed, ask the agent to "make a comparison" or "write a report" and it generates an `.html` file that opens in any browser with zero external dependencies.

## Install

```bash
npx skills add https://github.com/OiAnthony/html-effectiveness --skill html-effectiveness
```

## Templates

| Template | Use case |
|----------|----------|
| exploration | Side-by-side comparison of multiple options |
| code-review | PR / code walkthrough with diffs and annotations |
| report | Metric dashboard + timeline + sectioned prose |
| deck | Full-screen slides, arrow-key navigation |
| editor | Drag-and-drop editing with clipboard export |
| research | Long-form research with collapsible sections |
| changelog | Version history with category filters |

Not limited to these. When the content doesn't fit a template, the agent builds the page from the design system directly.

## Design system

Visual style from Kami "Parchment": warm cream background (`#f5f4ed`), ink-blue as the sole accent (`#1B365D`), Charter serif typeface, no bold or italic. Layout via Tailwind CSS v4 Play CDN, all styles inline, opens anywhere.

## Acknowledgments

- [html-effectiveness](https://github.com/ThariqS/html-effectiveness) by [Thariq Shihipar](https://x.com/trq212) — the original article and 20 HTML demos showing HTML as an AI output format. ([Live examples](https://thariqs.github.io/html-effectiveness/))
- [Kami (紙)](https://github.com/anthropics/kami) by [Tw93](https://github.com/Tw93) — a document typesetting skill, reference for design system and template structure.
- [AntV Infographic](https://github.com/antvis/infographic) by [AntV](https://github.com/antvis) — a declarative infographic engine, reference for chart generation patterns and visual language.
