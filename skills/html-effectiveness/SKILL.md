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
| Draw a diagram / flowchart | Illustration | Inline SVG, clean vector shapes |
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

## Design Quick Reference — Kami "Parchment" System

The full design system is in `references/design.md`. Templates use Tailwind CSS
v4 Play CDN with a `@theme` block that defines all Kami tokens.

### Tailwind CDN + Theme setup

Every HTML file must include this in `<head>`:

```html
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
<style type="text/tailwindcss">
  @theme {
    --color-parchment: #f5f4ed;
    --color-ivory: #faf9f5;
    --color-sand: #e8e6dc;
    --color-brand: #1B365D;
    --color-brand-light: #2D5A8A;
    --color-brand-tint: #EEF2F7;
    --color-brand-tint-strong: #E4ECF5;
    --color-near-black: #141413;
    --color-dark-warm: #3d3d3a;
    --color-olive: #504e49;
    --color-stone: #6b6a64;
    --color-border: #e8e6dc;
    --color-border-soft: #e5e3d8;
    --color-success: #4a7c59;
    --color-danger: #8b3a3a;
    --color-warning: #C78E3F;
    --color-dark-surface: #30302e;
    --color-deep-dark: #141413;
    --font-serif: Charter, Georgia, Palatino, "Times New Roman", serif;
    --font-sans: Charter, Georgia, Palatino, "Times New Roman", serif;
    --font-mono: "JetBrains Mono", "SF Mono", "Fira Code", Consolas, Monaco, monospace;
  }
</style>
```

### Color palette (Kami Parchment)

| Token | Hex | Usage |
|-------|-----|-------|
| `parchment` | `#f5f4ed` | Page background — warm cream |
| `ivory` | `#faf9f5` | Card / lifted container surface |
| `sand` | `#e8e6dc` | Button / interactive surface |
| `brand` | `#1B365D` | Ink Blue — sole accent, CTAs, section bar |
| `brand-light` | `#2D5A8A` | Links on dark, hover states |
| `brand-tint` | `#EEF2F7` | Lightest tag background |
| `brand-tint-strong` | `#E4ECF5` | Default tag background |
| `near-black` | `#141413` | Primary text |
| `dark-warm` | `#3d3d3a` | Secondary text, table headers |
| `olive` | `#504e49` | Subtext, descriptions |
| `stone` | `#6b6a64` | Tertiary, dates, metadata |
| `border` | `#e8e6dc` | Primary border |
| `border-soft` | `#e5e3d8` | Row separator |
| `success` | `#4a7c59` | Positive, additions |
| `danger` | `#8b3a3a` | Negative, deletions |
| `warning` | `#C78E3F` | Warning |
| `deep-dark` | `#141413` | Dark page background |
| `dark-surface` | `#30302e` | Dark container |

All grays are warm-toned (R >= G >= B). Never use cool/blue grays.

### Typography

Serif-led design: `--font-sans` equals `--font-serif` (Charter).

| Role | Size | Weight | Line-height | Tailwind |
|------|------|--------|-------------|----------|
| Display | 48px | 500 | 1.1 | `font-serif font-medium text-5xl leading-[1.1]` |
| H1 | 30px | 500 | 1.2 | `font-serif font-medium text-3xl` |
| H2 | 24px | 500 | 1.3 | `font-serif font-medium text-2xl` |
| H3 | 20px | 500 | 1.35 | `font-serif font-medium text-xl` |
| Lead | 16px | 400 | 1.5 | `.lead` (= `text-base`) |
| Body | 16px | 400 | 1.625 | `text-base leading-relaxed` (default, usually omit) |
| Small | 14px | 400 | 1.5 | `text-sm` |
| Eyebrow | 12px | 500 | 1.4 | `.eyebrow` (= `text-xs`) |
| Code | 12px | 400 | 1.65 | `font-mono text-xs leading-[1.65]` |

Rules:
- **Global styles on `<body>`, not per-element.** `font-family`, `font-size`, `line-height`, `color` these universally-applicable properties should be set once on `<body>` (e.g. `class="font-serif text-base leading-relaxed text-near-black"`). Only override at the element level when it actually differs from the default (headings, code blocks, captions). Never repeat `font-serif` on every `<p>` or `<div>`.
- **Prefer Tailwind preset values.** Use `text-xs` / `text-sm` / `text-base` / `text-lg` / `text-xl` … instead of arbitrary values like `text-[11px]` or `text-[13px]`. Arbitrary font sizes should only appear for Display/H1 when no preset matches.
- **Body defaults to `text-base` (16px).** Do not set smaller base font sizes like `text-[14px]` or `text-[15px]` — they hurt readability on most screens.
- **Serif everywhere** (sans = serif in Kami). Mono for labels/code/metadata.
- **No bold**: max weight is 500 for headings, 600 for labels. Never 700+.
- **No italic**: `font-style: italic` is forbidden.

### Spacing

Base unit: 4px. Use Tailwind spacing scale (1 = 4px).

| Context | Tailwind |
|---------|----------|
| Page padding | `px-8 pt-12 pb-24` |
| Section gap | `mb-12` |
| Card padding | `p-5` or `p-6` |
| Component gap | `gap-3` to `gap-4` |
| Max content width | `max-w-[1120px] mx-auto` |

### Shape

- Panel radius: `rounded-xl` (12px)
- Card/row radius: `rounded-lg` (8px)
- Tag radius: `rounded` (4px)
- Border: `border border-border`
- Shadows: whisper only — `hover:shadow-[0_1px_3px_rgba(20,20,19,0.06)]`

### Core component patterns (semantic classes)

Templates include semantic CSS classes via `assets/components.css` (injected by
`init.py`). These are **starting points, not constraints**. If a document needs
a component that doesn't exist — a radial progress ring, a comparison slider,
a node-graph legend — create it. The built-in classes cover common patterns;
the uncommon ones are where the most value lives. Follow the Kami design
tokens (colors, type, spacing, shape) but don't limit yourself to the
pre-built vocabulary.

Tailwind utilities are still used for layout (grid, flex, gap) and
one-off adjustments (margins, responsive prefixes).

**Defining new component classes:** The Tailwind v4 Play CDN supports `@apply`.
When a utility chain repeats 3+ times in your output, extract it as a class
inside the `<style type="text/tailwindcss">` block:

```css
.status-dot { @apply w-2 h-2 rounded-full bg-success; }
```

Then use `<span class="status-dot"></span>` everywhere instead of repeating the
utility chain. The built-in classes below are already defined this way.

**Surfaces:**
- `.card` (add `.card-lg` for 24px padding)
- `.callout` (muted bg) / `.callout-brand` (ivory bg + left-bar) / `.callout-light` (transparent bg + left-bar only — editorial style)

**Typography:**
- `.h2-bar` — Kami signature left-bar heading (rounded 1.5px)
- `.eyebrow` — Brand-colored mono label / `.eyebrow-muted` — Stone-colored
- `.lead` — Large intro paragraph (16px, dark-warm, max-width 85%)
- `.hl` — Brand-color inline highlight (text-brand font-medium)
- `.sub` — Small annotation next to headings

**Tags & Badges:**
- `.tag` / `.tag-breaking` (warm red for breaking changes)
- `.badge` (variants: `.badge-success`, `.badge-danger`, `.badge-warning`)
- `.section-num`

**Metrics (Kami inline strip):**
- `.metrics` — Horizontal flex row with dotted bottom border
- `.metric` — Single metric (flex baseline, transparent)
- `.metric-value` — Large brand number (24px, tabular-nums)
- `.metric-label` — Small olive label

**Timeline:**
- `.timeline` — Horizontal flex row
- `.tl-step` / `.tl-year` / `.tl-head` / `.tl-body`

**Lists:**
- `ul.dash` — Em-dash list with brand-colored markers

**Tables:**
- `.kami-table` — Polished table (dotted row borders)
- Variants: `.compact`, `.striped`, `.financial`
- `.total` on `<tr>` for summary rows

**Quote:**
- `.quote` — Left-bar blockquote with `.cite` for attribution

**Layout:**
- `.two-col` — Two-column grid

**Buttons:**
- `.btn-primary` / `.btn-ghost`

**Code:**
- `.inline-code` / `.code-block`

**Footer:**
- `.doc-footer` — Dotted-top separator with left/right spans

**Version (Changelog):**
- `.version-header` with `.version-logo`, `.version-title`, `.version-tagline`, `.version-date`

**Provenance & Indicators:**
- `.prompt-box` — Shows the prompt that generated this document (`.prompt-label` for the mono label)
- `.chip` — Compact mono-font pill for at-a-glance metrics (`.chip-val` for the emphasized value)

Example — metric strip:
```html
<div class="metrics">
  <div class="metric">
    <span class="metric-value">24</span>
    <span class="metric-label">Open issues</span>
  </div>
</div>
```

Example — numbered section:
```html
<h2 class="h2-bar text-2xl tracking-tight mb-2">1. Title</h2>
```

Example — callout-light:
```html
<div class="callout-light">
  <div class="eyebrow mb-1">Key Takeaway</div>
  <p class="text-dark-warm">Content here.</p>
</div>
```

Example — prompt box (exploration / research header):
```html
<div class="prompt-box">
  <span class="prompt-label">Prompt</span>
  Show me three ways to implement debounced search with tradeoffs.
</div>
```

Example — chip strip (inside comparison cards):
```html
<div class="flex flex-wrap gap-2">
  <span class="chip">Bundle: <span class="chip-val">+0 kb</span></span>
  <span class="chip">Reuse: <span class="chip-val">high</span></span>
</div>
```

**Tab active**: `text-near-black border-b-2 border-brand`
**Tab inactive**: `text-stone border-b-2 border-transparent hover:text-near-black`

### Design invariants

1. Page background is parchment (never pure white)
2. All grays are warm-toned (R >= G >= B)
3. Single accent: brand (#1B365D)
4. Serif-led typography (sans = serif)
5. No bold (max weight 500), no italic
6. Shadows are whisper-only
7. Section titles use left-bar (`.h2-bar`)
8. Separators are dotted (not solid) — `border-dotted border-border`
9. Numbers use `font-variant-numeric: tabular-nums`
10. Tailwind utility-first with semantic classes for repeated patterns

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

### Interaction recipes

Beyond the basic patterns (tabs, drag-and-drop, slides), these recipes add
tangible delight and comprehension value. Use them when the document type
calls for it — don't force them everywhere.

**Hover-linked glossary** (research / explainer):
Place a sticky `<aside>` sidebar with a `<dl>` of key terms. In the body text,
wrap terms in `<span class="term" data-term="ring">`. On hover, highlight the
matching `<dt>` in the sidebar. This turns unfamiliar vocabulary into something
the reader can touch without interrupting their reading flow.

```javascript
document.querySelectorAll('.term').forEach(function(el) {
  var g = el.dataset.term;
  el.addEventListener('mouseenter', function() {
    document.querySelector('dt[data-g="' + g + '"]')?.classList.add('hl');
  });
  el.addEventListener('mouseleave', function() {
    document.querySelector('dt[data-g="' + g + '"]')?.classList.remove('hl');
  });
});
```

Style the `.term` span with `border-bottom: 1.5px dotted; cursor: help` and
the `.hl` state on the sidebar `<dt>` with a subtle brand-tint background.

**CSS custom-property live tuning** (prototype / animation sandbox):
Define adjustable parameters as CSS custom properties on `:root`, then let
sliders or preset buttons swap them via `setProperty()`. Every transition and
animation on the page reacts instantly — zero re-render, zero JS animation
libraries.

```javascript
var root = document.documentElement;
slider.addEventListener('input', function() {
  root.style.setProperty('--duration', slider.value + 'ms');
});
presetBtn.addEventListener('click', function() {
  root.style.setProperty('--ease', btn.dataset.ease);
});
```

**Dim-not-hide filtering** (editor / triage board):
When filtering by tag or category, don't hide non-matching items — set them to
`opacity: 0.25`. This preserves spatial context so the user still sees the
overall landscape. Show a colored filter pill in the toolbar that clears the
filter on click.

**Micro-delight animations** (prototype / editor):
CSS-only confetti, checkmark draw-on, or scale-bounce on state change. These
take 10-15 lines of CSS and zero JS, but make the interaction *feel* rewarding.
Use sparingly — one micro-animation per document, tied to the primary action.

```css
/* Example: 6 confetti particles on task completion */
.confetti { position: absolute; width: 6px; height: 6px; border-radius: 2px; opacity: 0; }
.done .confetti { animation: pop 520ms var(--ease) 200ms forwards; }
@keyframes pop {
  0%   { opacity: 0; transform: translate(0,0) scale(0.6); }
  15%  { opacity: 1; }
  100% { opacity: 0; transform: translate(var(--dx),var(--dy)) rotate(var(--rot)) scale(1); }
}
```

Set `--dx`, `--dy`, `--rot` per particle via inline style or numbered classes.

### Inline SVG diagrams

Use inline `<svg>` for architecture diagrams, data-flow charts, flowcharts,
and concept illustrations. SVG gives pixel-precise control, scales to any
screen, and uses the same Kami color tokens as the rest of the page.

**Arrow marker definition** — put this once in `<defs>`, reuse everywhere:

```html
<svg viewBox="0 0 860 340" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="7" markerHeight="7" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#6b6a64"/>
    </marker>
    <!-- accent arrow for highlighted paths -->
    <marker id="arrow-brand" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="7" markerHeight="7" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#1B365D"/>
    </marker>
  </defs>
```

**Box node** — rounded rect + centered title + subtitle:

```html
<rect x="20" y="20" width="180" height="54" rx="10"
      fill="#faf9f5" stroke="#e8e6dc" stroke-width="1.5"/>
<text x="110" y="43" text-anchor="middle"
      font-size="12" font-weight="500" fill="#141413">Service Name</text>
<text x="110" y="60" text-anchor="middle"
      font-size="10.5" fill="#6b6a64">packages/api</text>
```

**Dark box** for databases / storage:

```html
<rect x="340" y="266" width="180" height="54" rx="10"
      fill="#141413" stroke="#141413"/>
<text x="430" y="289" text-anchor="middle"
      font-size="12" font-weight="500" fill="#faf9f5">comments table</text>
<text x="430" y="306" text-anchor="middle"
      font-size="10.5" fill="#C9B98A">postgres</text>
```

**Connections** — solid for sync, dashed for async:

```html
<!-- sync flow -->
<path d="M200 177 L340 177" stroke="#6b6a64" stroke-width="1.5"
      fill="none" marker-end="url(#arrow)"/>
<!-- async / optional flow -->
<path d="M520 177 L660 177" stroke="#1B365D" stroke-width="1.5"
      fill="none" stroke-dasharray="5 4" marker-end="url(#arrow-brand)"/>
```

**Annotations** — plain text placed near the relevant element:

```html
<text x="415" y="234" text-anchor="middle"
      font-size="12" fill="#6b6a64">next to run</text>
```

**Key rules**:
- `viewBox` with fixed coordinates (e.g. `0 0 860 340`), let the SVG scale
  responsively via `width="100%"` on the containing element
- Strokes: `1.5px` normal, `2px` for emphasized elements
- All corners rounded: `rx="10"` on rects
- Fonts inside SVG: use `font-family` matching the page mono/sans stack
- Colors: use Kami hex values directly (CSS custom properties don't work
  reliably inside inline SVG across all browsers)
- Wrap each diagram in a `<figure>` with `<figcaption>` for context

**Figure wrapper**:

```html
<figure>
  <div class="card p-0 overflow-hidden">
    <svg viewBox="0 0 860 340" xmlns="http://www.w3.org/2000/svg">
      <!-- diagram content -->
    </svg>
  </div>
  <figcaption class="text-sm text-stone mt-2">
    Data flow: optimistic write path on the left, fan-out on the right.
  </figcaption>
</figure>
```

---

## JavaScript patterns

### Data-driven rendering

Define data at the top, render from it. This is the single most important JS
pattern — it keeps content separate from presentation and makes export trivial.

```javascript
var DATA = [
  { id: 'T-101', title: 'Fix auth flow', priority: 'high', status: 'open' },
  // ...
];

function render() {
  container.innerHTML = '';
  DATA.forEach(function(item) {
    var el = document.createElement('div');
    el.className = 'card';
    el.innerHTML = '<h3>' + item.title + '</h3>';
    container.appendChild(el);
  });
}
render();
```

### Clipboard export

Every editor must have an export button. Use this pattern:

```javascript
function buildExport() {
  return JSON.stringify(DATA, null, 2);
  // or build Markdown, CSV, etc.
}

exportBtn.addEventListener('click', function() {
  navigator.clipboard.writeText(buildExport()).then(function() {
    exportBtn.textContent = 'Copied';
    exportBtn.classList.add('copied');
    setTimeout(function() {
      exportBtn.textContent = 'Copy';
      exportBtn.classList.remove('copied');
    }, 2000);
  });
});
```

### Closed-loop workflow

HTML artifacts are not just output — they are a **bidirectional interface**
between the agent and the human. The user reads, adjusts, exports, and pastes
the result back into the agent for the next iteration.

Design every interactive artifact with this loop in mind:

```
Agent generates HTML → User opens and adjusts → Export button → Clipboard
→ User pastes back into agent → Agent uses exported data → next iteration
```

Practical implications:

1. **Design the export format first.** Before building the editor, decide what
   the agent or the codebase needs: Markdown table? JSON config? A prompt with
   the user's choices filled in? Build the `buildExport()` function first, then
   design the UI that produces that output.

2. **Use `.prompt-box`** at the top of exploration and research documents to
   show the prompt that generated them. This lets the user copy-and-modify the
   prompt for a follow-up round.

3. **Export as prompt** is often more useful than export as data. For a triage
   board, exporting "Move BIR-241 to Now because…" as a prompt the user can
   paste back is more actionable than a raw JSON dump.

4. **Multiple export formats** when the audience varies: "Copy as Markdown"
   for pasting into a planning doc, "Copy as JSON" for committing to config,
   "Copy as Prompt" for continuing the conversation with the agent.

### Drag and drop

For triage boards and reorderable lists:

```javascript
card.draggable = true;
card.addEventListener('dragstart', function(e) {
  e.dataTransfer.setData('text/plain', item.id);
  card.classList.add('dragging');
});
dropZone.addEventListener('dragover', function(e) { e.preventDefault(); });
dropZone.addEventListener('drop', function(e) {
  e.preventDefault();
  var id = e.dataTransfer.getData('text/plain');
  // move item, re-render
});
```

### Tab navigation

```javascript
tabs.forEach(function(tab) {
  tab.addEventListener('click', function() {
    tabs.forEach(function(t) { t.classList.remove('active'); });
    tab.classList.add('active');
    panels.forEach(function(p) { p.style.display = 'none'; });
    document.getElementById(tab.dataset.panel).style.display = 'block';
  });
});
```

### Slide deck (arrow keys)

```css
body { scroll-snap-type: y mandatory; overflow-y: scroll; }
.slide { width: 100vw; height: 100vh; scroll-snap-align: start; }
```

```javascript
document.addEventListener('keydown', function(e) {
  if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
    e.preventDefault();
    currentSlide = Math.min(currentSlide + 1, slides.length - 1);
    slides[currentSlide].scrollIntoView({ behavior: 'smooth' });
  }
});
```

---

## Common mistakes to avoid

- **Unauthorized externals**: Only Tailwind CSS Play CDN is allowed. No Google Fonts, no other JS libraries, no other CSS frameworks.
- **Cool grays**: Never use `#f8f9fa`, `#e9ecef`, or any blue-tinted gray. Stick to the warm Kami palette.
- **Bold/italic**: No `font-weight: 700` or `font-style: italic`. Max weight is 500-600.
- **Hard shadows**: No `box-shadow: 0 2px 8px rgba(0,0,0,0.3)`. Only whisper shadows.
- **Missing export**: Every interactive editor needs a clipboard export button.
- **Non-semantic HTML**: Use proper elements — `<table>` for tabular data, `<ul>` for lists, not divs for everything.
- **Forgetting responsive**: Use Tailwind `max-md:` prefix for narrower screens.
- **Raw data dump**: Structure the data visually. Use grids, cards, badges, color coding. The whole point is to make information *scannable*.
- **Wrong accent color**: The sole accent is ink-blue (`brand` / `#1B365D`). Never use clay, orange, or other warm accents as the primary color.

