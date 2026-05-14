---
name: html-effectiveness
description: >-
  Generate rich, interactive, self-contained HTML artifacts instead of Markdown.
  Use this skill whenever the user asks for visual output that Markdown can't
  express well — explorations, code reviews, design systems, prototypes,
  research reports, slide decks, diagrams, status reports, or custom editing
  interfaces (triage boards, feature-flag editors, prompt tuners). Also use when
  the user says "make an HTML file", "make an artifact", "visualize this",
  "show me a comparison", or asks for anything interactive, spatial, or
  presentation-quality. Even if the user just asks for a "report" or "summary",
  consider whether HTML would serve them better than Markdown — if the content
  has tables, metrics, code diffs, timelines, or multiple sections, it almost
  certainly will.
---

# HTML Effectiveness

You produce **single self-contained HTML files** — inline CSS and JS, no external
dependencies, no build step. The output opens in any browser and looks polished
enough to share.

HTML takes 2-4x more tokens than Markdown, but the payoff is enormous: richer
information density, spatial layout, interactivity, and outputs people actually
*read*. Markdown is fine for short answers. For anything with structure, data,
comparisons, or interaction — use HTML.

## When to choose HTML over Markdown

- Comparing 2+ options side by side (approaches, designs, tradeoffs)
- Code diffs, PR reviews, annotated code walkthrough
- Anything with metrics, KPIs, or dashboards
- Implementation plans with phases, dependencies, status
- Research with tabs, collapsible sections, cross-references
- Slide decks or presentations
- SVG diagrams, flowcharts, architecture maps
- Interactive editors (triage boards, config editors, prompt tuners)
- Status reports, incident timelines, changelogs
- Design systems, component showcases

When in doubt, choose HTML.

---

## Step 1 — Decide the language

**Match the user's language.** All text content inside the HTML — headings,
paragraphs, labels, tooltips, button text — must be in the same language the
user is writing in. Code identifiers and technical terms stay in their original
form.

When ambiguous (e.g. a single URL with no surrounding text), ask a one-liner
rather than guess.

| User language | `<html lang>` | Content language | UI chrome |
|---|---|---|---|
| Chinese | `zh-CN` | Chinese | Chinese |
| English | `en` | English | English |
| Other (best-effort) | appropriate BCP 47 tag | match user | match user |

## Step 2 — Pick the document type

Read `references/categories.md` for the full catalog of 10 categories and their
use cases. Here is the quick decision table:

| User intent | Category | Key pattern |
|-------------|----------|-------------|
| Compare approaches / options | Exploration | Side-by-side cards or columns |
| Review PR / explain code | Code Review | Diff view, annotation bubbles |
| Show design tokens / components | Design | Swatch grids, component stages |
| Prototype animation / interaction | Prototype | Live controls, sliders, preview pane |
| Explain a concept / feature | Research | Collapsible sections, progressive disclosure, inline demos |
| Status update / incident report | Report | Metric strip, timeline, status badges |
| Present to an audience | Deck | Full-viewport slides, arrow-key nav |
| Draw a diagram / flowchart | Illustration | Mermaid code blocks via beautiful-mermaid |
| Build a throwaway editing tool | Editor | Data-driven DOM, drag-and-drop, export |
| Release notes / version history | Changelog | Categorized entries with filters |

## Step 3 — Read the design reference

Before writing any HTML, read `references/design.md`. It contains the complete
design system: color tokens, typography scale, spacing, component recipes, and
the design invariants you must follow. This is the foundation — every HTML file
you produce must use these tokens and patterns.

## Step 4 — Scaffold via script (mandatory)

**Always** use `scripts/init.py` to create the HTML file. This avoids
outputting the full template skeleton as tokens.

```bash
python3 scripts/init.py <template> "<title>" [--subtitle "..."] [--eyebrow "..."] [-o ./output.html]
```

Available templates (`python3 scripts/init.py --list`):
- `exploration` — Side-by-side comparison layout with metrics strip
- `code-review` — Diff view with annotations and file tabs
- `report` — Metrics strip + horizontal timeline + sections
- `deck` — Full-screen slide deck with keyboard navigation
- `editor` — Interactive editor with drag-and-drop and export
- `research` — Long-form research with collapsible sections
- `changelog` — Version changelog with category filters

The script writes the file to the current working directory by default
(filename derived from title). Pass `-o path` to override.

If **no template matches**, start from the design tokens in `references/design.md`
and build the layout yourself — this is the only case where you write HTML from
scratch.

## Step 5 — Fill the scaffolded file (chunked generation)

Open the file created by `init.py` and fill it with real content. **Never
generate the entire document in a single Edit call.** Split the work by
section so each write is short and the user sees steady progress.

### 5a — Plan the chunks

Analyze the source content and identify logical sections (tabs, chapters,
card groups, slide batches). Typical split points:

| Template | Natural chunk unit |
|----------|-------------------|
| research / exploration | One tab panel per chunk |
| report | Metric strip as chunk 1, then each section |
| deck | 3-5 slides per chunk |
| code-review | One file tab per chunk |
| editor | Data definition as chunk 1, then render logic |
| changelog | Version header + each category section |

Create a task for each chunk using TaskCreate (subject = section name,
activeForm = "Filling: <section name>"). This gives the user a progress bar.

### 5b — Fill one chunk at a time

For each task/chunk:
1. Mark the task `in_progress`
2. Edit the HTML file — replace the relevant placeholder or append the section
   content. **Keep each Edit under ~300 lines of new HTML.**
3. Mark the task `completed`
4. Move to the next chunk

If a section is still too large (> 300 lines), split it further into
sub-sections within the same Edit pass.

### 5c — Small document shortcut

If the total content to fill is clearly < 300 lines of HTML (e.g. a simple
3-card comparison, a short 5-slide deck), you may skip chunking and fill
everything in a single Edit. Use judgment — the goal is to avoid output stalls,
not to add ceremony to trivial tasks.

### Key rules (apply to every chunk)

- **Self-contained**: Everything inline except Tailwind CSS Play CDN. No other
  external dependencies.
- **Tailwind CSS**: Always include `<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>`
  and a `<style type="text/tailwindcss">` block with the `@theme` tokens.
- **Semantic HTML5**: Use `<header>`, `<section>`, `<article>`, `<aside>`, `<nav>`.
- **Data-driven JS**: Define data as a JS object/array at the top of `<script>`,
  then render from it. This makes the content easy to update.
- **Export button**: Any editor or interactive tool MUST end with an export
  button that copies data as JSON, Markdown, or a prompt to clipboard.
- **Responsive**: Support down to ~800px width. Use Tailwind responsive prefixes.
- **No italic**: Never use `font-style: italic`.

## Step 6 — Open the file

The file was already saved by `init.py` in Step 4. After editing, open it:
```bash
open <filename>.html
```

---

## Design system

Read `references/design.md` for the complete Kami design system: color tokens,
`@theme` block, typography scale, spacing, shape, and component class catalog.

### Design invariants (always enforce)

1. Page background is parchment (`#f5f4ed`) — never pure white
2. All grays are warm-toned (R >= G >= B) — no cool/blue grays
3. Single accent: brand (`#1B365D`)
4. Serif-led typography (sans = serif = Charter)
5. No bold (max weight 500-600), no italic
6. Shadows are whisper-only
7. Section titles use left-bar (`.h2-bar`)
8. Separators are dotted (not solid) — `border-dotted border-border`
9. Numbers use `font-variant-numeric: tabular-nums`
10. Tailwind utility-first with semantic classes for repeated patterns
11. Body defaults to `text-base` (16px) — never set smaller base sizes
12. Global styles on `<body>`, not per-element

### Component classes

Templates include `assets/components.css` (injected by `init.py`). These are
starting points — create new components freely using Kami tokens. Extract
repeated utility chains as `@apply` classes in the `<style>` block.

Key classes: `.card`, `.callout-light`, `.h2-bar`, `.eyebrow`, `.lead`,
`.metrics` + `.metric-value` + `.metric-label`, `.tag`, `.badge`,
`.kami-table`, `.btn-primary`, `.prompt-box`, `.chip`, `.doc-footer`

See `references/design.md` for the full class catalog with examples.

---

## Interaction design principles

**Continuous scroll by default.** Content sections render top-to-bottom in a
single page — never hide body content behind tabs to save height. Readers should
see the full structure and scale of the document at a glance.

**Tabs are for state switching only.** Use tabs when the user needs to toggle
between distinct states: switching files in a code review, filtering changelog
categories, comparing two versions of an output. If the "tabs" are just chapter
headings that could be `<h2>` sections, use `<h2>` sections.

**Every interaction must serve comprehension.** Before adding a control, ask:
does clicking this help the reader understand faster than scrolling would?
Good examples:
- `<details>` for supplementary info the reader may skip (progressive disclosure)
- Click-to-reveal on diagram nodes to show inline context
- Side-by-side cards for simultaneous comparison
- Live sliders/buttons to let the user *feel* parameter changes
- Drag-and-drop to let the user rearrange and export a result

Bad examples:
- Tabs that split an article into "pages" just to shorten the scroll
- Accordions that collapse every section — forcing N clicks to read N sections
- Modals that interrupt reading flow for non-critical content

For advanced interaction recipes (hover-linked glossary, CSS custom-property
live tuning, dim-not-hide filtering, micro-delight animations), see
`references/interaction-recipes.md`.

### Diagrams — Mermaid via beautiful-mermaid

Use beautiful-mermaid for all diagrams. Write Mermaid syntax in
`<div class="mermaid">` — the library renders styled SVG automatically.
Templates already include the rendering script (`assets/mermaid.html`).

```html
<figure class="diagram">
  <div class="mermaid">
graph TD
  A[User Request] --> B{Route}
  B -->|Docs| C[Kami]
  B -->|Code| D[Kaku]
  </div>
  <figcaption>Request routing overview.</figcaption>
</figure>
```

Rules: wrap in `<figure class="diagram">` + `<figcaption>`; keep ≤12 nodes;
use subgraphs for grouping; label edges with the relationship.

For supported types, syntax, theme mapping, and examples see
`references/beautiful-mermaid.md`.

---

## JavaScript patterns

Key principles:
- **Data-driven**: Define data as a JS array/object at the top, render from it
- **Clipboard export**: Every editor needs a "Copy" button (JSON, Markdown, or prompt)
- **Closed-loop**: Design artifacts as bidirectional — user adjusts, exports,
  pastes back into the agent for the next iteration
- **Export as prompt** is often more useful than export as data

For implementation patterns (data-driven rendering, clipboard export,
drag-and-drop, tab navigation, slide deck), see `references/js-patterns.md`.

---

## Common mistakes to avoid

- **Unauthorized externals**: Only Tailwind CSS Play CDN and `esm.sh/beautiful-mermaid` are allowed. No Google Fonts, no other JS libraries, no other CSS frameworks.
- **Cool grays**: Never use `#f8f9fa`, `#e9ecef`, or any blue-tinted gray. Stick to the warm Kami palette.
- **Bold/italic**: No `font-weight: 700` or `font-style: italic`. Max weight is 500-600.
- **Hard shadows**: No `box-shadow: 0 2px 8px rgba(0,0,0,0.3)`. Only whisper shadows.
- **Missing export**: Every interactive editor needs a clipboard export button.
- **Non-semantic HTML**: Use proper elements — `<table>` for tabular data, `<ul>` for lists, not divs for everything.
- **Forgetting responsive**: Use Tailwind `max-md:` prefix for narrower screens.
- **Raw data dump**: Structure the data visually. Use grids, cards, badges, color coding. The whole point is to make information *scannable*.
- **Wrong accent color**: The sole accent is ink-blue (`brand` / `#1B365D`). Never use clay, orange, or other warm accents as the primary color.

