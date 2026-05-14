# Design System Reference — Kami "Parchment"

Complete design token reference for HTML artifacts. Based on the Kami design
system. Every HTML file produced by this skill must use these tokens via
Tailwind CSS v4 Play CDN.

---

## Setup

Every HTML file includes Tailwind CSS and defines the theme:

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
    --font-serif: "TsangerJinKai02", "Source Han Serif SC", "Noto Serif CJK SC", "Songti SC", Charter, Georgia, serif;
    --font-sans: "TsangerJinKai02", "Source Han Serif SC", "Noto Serif CJK SC", "Songti SC", Charter, Georgia, serif;
    --font-mono: "JetBrains Mono", "SF Mono", "Fira Code", Consolas, Monaco, "TsangerJinKai02", "Source Han Serif SC", monospace;
  }
</style>
```

---

## Color palette

Warm parchment aesthetic. All grays have a yellow-brown undertone (R >= G >= B).
Never use cool/blue grays like Bootstrap's `#f8f9fa` or `#dee2e6`.

### Surfaces

| Token | Hex | Tailwind | Usage |
|-------|-----|----------|-------|
| `parchment` | `#f5f4ed` | `bg-parchment` | Page background — warm cream |
| `ivory` | `#faf9f5` | `bg-ivory` | Card / lifted container |
| `sand` | `#e8e6dc` | `bg-sand` | Button / interactive surface |

### Brand (sole accent — 5% of surface max)

| Token | Hex | Tailwind | Usage |
|-------|-----|----------|-------|
| `brand` | `#1B365D` | `text-brand`, `bg-brand`, `border-brand` | Ink Blue — CTAs, section bar, accents |
| `brand-light` | `#2D5A8A` | `text-brand-light` | Links on dark surfaces, hover |
| `brand-tint` | `#EEF2F7` | `bg-brand-tint` | Lightest tag background |
| `brand-tint-strong` | `#E4ECF5` | `bg-brand-tint-strong` | Default tag background |

### Text hierarchy

| Token | Hex | Tailwind | Usage |
|-------|-----|----------|-------|
| `near-black` | `#141413` | `text-near-black` | Primary text |
| `dark-warm` | `#3d3d3a` | `text-dark-warm` | Secondary text, table headers |
| `olive` | `#504e49` | `text-olive` | Subtext, descriptions |
| `stone` | `#6b6a64` | `text-stone` | Tertiary, dates, metadata |

### Borders

| Token | Hex | Tailwind | Usage |
|-------|-----|----------|-------|
| `border` | `#e8e6dc` | `border-border` | Primary border |
| `border-soft` | `#e5e3d8` | `border-border-soft` | Row separator |

### Semantic

| Token | Hex | Tailwind | Usage |
|-------|-----|----------|-------|
| `success` | `#4a7c59` | `text-success` | Positive, additions |
| `danger` | `#8b3a3a` | `text-danger` | Negative, deletions |
| `warning` | `#C78E3F` | `text-warning` | Warning |

### Dark mode

| Token | Hex | Tailwind | Usage |
|-------|-----|----------|-------|
| `deep-dark` | `#141413` | `bg-deep-dark` | Dark page background |
| `dark-surface` | `#30302e` | `bg-dark-surface` | Dark container |

---

## Typography

Serif-led design. `--font-sans` is aliased to `--font-serif`
(TsangerJinKai02), so the entire page uses serif. Mono for code/labels/metadata.

### Font stacks

```
serif/sans: "TsangerJinKai02", "Source Han Serif SC", "Noto Serif CJK SC", "Songti SC", Charter, Georgia, serif
mono:       "JetBrains Mono", "SF Mono", "Fira Code", Consolas, Monaco, "TsangerJinKai02", "Source Han Serif SC", monospace
```

### Type scale

| Role | Size | Weight | Line-height | Tailwind |
|------|------|--------|-------------|----------|
| Display | 48px | 500 | 1.1 | `font-serif font-medium text-5xl leading-[1.1] tracking-tight` |
| H1 | 30px | 500 | 1.2 | `font-serif font-medium text-3xl tracking-tight` |
| H2 | 24px | 500 | 1.3 | `font-serif font-medium text-2xl` |
| H3 | 20px | 500 | 1.35 | `font-serif font-medium text-xl` |
| Body | 16px | 400 | 1.55 | `text-base leading-relaxed` |
| Small | 14px | 400 | 1.5 | `text-sm` |
| Eyebrow | 11px | 500 | 1.4 | `font-mono text-xs tracking-[0.08em] uppercase` |
| Code | 12.5px | 400 | 1.65 | `font-mono text-xs leading-[1.65]` |

### Rules

- **Global styles on body**: Set `font-family`, `font-size`, `line-height`, `color` on `<body>` once. Only override per-element when actually different. Never repeat `font-serif` on every `<p>`.
- **Serif everywhere**: sans = serif in this system. No system UI fonts.
- **No bold**: maximum weight is 500 for headings, 600 for labels. Never use 700+.
- **No italic**: `font-style: italic` is forbidden.
- **Eyebrow labels**: always `uppercase tracking-[0.08em]`.
- **Antialiasing**: always set `antialiased` on body.
- **Prefer Tailwind presets**: Use `text-xs`/`text-sm`/`text-base`/`text-lg`/`text-xl` instead of arbitrary values like `text-[11px]`. Arbitrary sizes only for Display when no preset matches.

---

## Spacing

Base unit: 4px. Tailwind's default scale (1 = 4px) aligns perfectly.

| Context | Tailwind |
|---------|----------|
| Page padding | `px-8 pt-12 pb-24` |
| Section gap | `mb-12` |
| Card padding | `p-5` or `p-6` |
| Component gap | `gap-3` to `gap-4` |
| Max content width | `max-w-[1120px] mx-auto` |

---

## Shape

| Element | Radius | Tailwind |
|---------|--------|----------|
| Panel / card | 12px | `rounded-xl` |
| Row / input | 8px | `rounded-lg` |
| Tag | 4px | `rounded` |
| Button (action) | pill | `rounded-full` |

### Border

Standard: `border border-border`

### Shadow

Whisper shadow only — no hard drop shadows.

| Level | Tailwind / CSS |
|-------|----------------|
| Hover lift | `hover:shadow-[0_1px_3px_rgba(20,20,19,0.06)]` |
| Card hover | `hover:shadow-[0_4px_24px_rgba(0,0,0,0.05)]` |

---

## Component recipes

Components use semantic CSS classes from `assets/components.css`, injected
automatically by `init.py`. Tailwind utilities handle layout and one-off spacing.

### Header

```html
<header>
  <div class="eyebrow">CATEGORY</div>
  <h1 class="font-medium text-3xl tracking-tight mt-1.5 mb-1">Title</h1>
  <p class="text-stone max-w-[620px]">Description</p>
</header>
```

### Section heading (Kami signature left-bar)

```html
<h2 class="h2-bar">Title</h2>
```

### Numbered section

```html
<h2 class="h2-bar text-2xl tracking-tight mb-2">1. Title</h2>
```

### Lead paragraph

```html
<p class="lead">Summary text that introduces the document section.</p>
```

### Metrics strip (inline, transparent)

```html
<div class="metrics">
  <div class="metric">
    <span class="metric-value">3</span>
    <span class="metric-label">Options</span>
  </div>
  <div class="metric">
    <span class="metric-value">Med</span>
    <span class="metric-label">Complexity</span>
  </div>
</div>
```

### Metric cards (boxed variant)

```html
<div class="grid grid-cols-4 gap-4 max-md:grid-cols-2">
  <div class="card">
    <div class="metric-val">24</div>
    <div class="metric-label">Open issues</div>
  </div>
</div>
```

### Card

```html
<div class="card hover:border-stone transition-colors">
  <h3 class="font-medium text-xl mb-2">Title</h3>
  <p class="text-dark-warm">Content</p>
</div>
```

### Tag

```html
<span class="tag">Label</span>
```

### Badge

```html
<span class="badge">Status</span>
```

Badge variants:
- Success: `badge badge-success`
- Danger: `badge badge-danger`
- Warning: `badge badge-warning`

### Button primary

```html
<button class="btn-primary">Action</button>
```

### Button ghost

```html
<button class="btn-ghost">Cancel</button>
```

### Code block (dark)

```html
<div class="code-block">
  <!-- code content -->
</div>
```

Syntax colors:
```css
.code .kw  { color: #1B365D; }  /* keywords — brand */
.code .str { color: #4a7c59; }  /* strings — success */
.code .cm  { color: #6b6a64; }  /* comments — stone */
.code .fn  { color: #C9B98A; }  /* functions — warm gold */
.code .num { color: #2D5A8A; }  /* numbers — brand-light */
```

### Inline code

```html
<code class="inline-code">functionName</code>
```

### Callout (brand — filled background)

```html
<div class="callout-brand text-dark-warm">
  Callout content
</div>
```

### Callout (light — transparent with left bar only)

```html
<div class="callout-light">
  <div class="eyebrow mb-1">Key Insight</div>
  <p class="text-dark-warm">Content here.</p>
</div>
```

### Timeline (horizontal)

```html
<div class="timeline">
  <div class="tl-step">
    <div class="tl-year">2024-01</div>
    <div class="tl-head">Phase One</div>
    <div class="tl-body">Description of this step.</div>
  </div>
  <div class="tl-step">
    <div class="tl-year">2024-03</div>
    <div class="tl-head">Phase Two</div>
    <div class="tl-body">Description of this step.</div>
  </div>
</div>
```

### Dash list

```html
<ul class="dash text-dark-warm">
  <li>First item</li>
  <li>Second item</li>
</ul>
```

### Quote

```html
<div class="quote">
  <p class="text-dark-warm">"Quoted text here."</p>
  <cite class="text-sm text-stone mt-1 block">— Source</cite>
</div>
```

### Kami table

```html
<table class="kami-table">
  <thead>
    <tr><th>Header</th><th>Header</th></tr>
  </thead>
  <tbody>
    <tr><td>Cell</td><td>Cell</td></tr>
  </tbody>
</table>
```

### Version header (changelog)

```html
<div class="version-header">
  <div class="version-logo">Project Name</div>
  <div class="version-title">v2.0 "Codename"</div>
  <div class="version-tagline">One-line summary</div>
  <div class="version-date">May 2026</div>
</div>
```

### Prompt box

Show the prompt that generated this document. Useful in exploration and
research artifacts to give the reader context on how the document was created.

```html
<div class="prompt-box">
  <span class="prompt-label">Prompt</span>
  Show me three different ways to implement debounced search for the task
  filter input, with tradeoffs for each.
</div>
```

### Chip (compact indicator)

Small mono-font pills for at-a-glance metrics inside cards. Use a row of
chips to show dimensions like bundle size, testability, reuse, SSR safety.

```html
<div class="flex flex-wrap gap-2">
  <span class="chip">Bundle: <span class="chip-val">+0 kb</span></span>
  <span class="chip">Testability: <span class="chip-val">high</span></span>
  <span class="chip">Reuse: <span class="chip-val">medium</span></span>
</div>
```

### Inline SVG diagram

Box-and-arrow diagrams for architecture, data flow, and process
visualization. Wrap in `<figure>` with a caption.

```html
<figure>
  <div class="card p-0 overflow-hidden">
    <svg viewBox="0 0 720 280" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5"
                markerWidth="7" markerHeight="7" orient="auto">
          <path d="M0,0 L10,5 L0,10 z" fill="#6b6a64"/>
        </marker>
      </defs>
      <rect width="720" height="280" fill="#faf9f5"/>
      <!-- service node -->
      <rect x="40" y="40" width="160" height="50" rx="10"
            fill="#faf9f5" stroke="#e8e6dc" stroke-width="1.5"/>
      <text x="120" y="62" text-anchor="middle"
            font-size="12" font-weight="500" fill="#141413">API Gateway</text>
      <text x="120" y="78" text-anchor="middle"
            font-size="10.5" fill="#6b6a64">packages/gateway</text>
      <!-- connection -->
      <path d="M200 65 L300 65" stroke="#6b6a64" stroke-width="1.5"
            fill="none" marker-end="url(#arrow)"/>
    </svg>
  </div>
  <figcaption class="text-sm text-stone mt-2">Request flow through the API gateway.</figcaption>
</figure>
```

### Document footer

```html
<div class="doc-footer">
  <span>Project description</span>
  <span>URL or attribution</span>
</div>
```

### Highlight span

```html
<span class="hl">highlighted text</span>
```

### Two-column layout

```html
<div class="two-col">
  <div>Left column content</div>
  <div>Right column content</div>
</div>
```

### Flow steps (horizontal process)

For CI/CD pipelines, migration plans, user journeys — any ordered 3-6 step
process. Uses existing `.section-num` for step markers.

```html
<div class="flex items-start gap-0">
  <div class="flex-1 text-center">
    <span class="section-num">01</span>
    <div class="text-sm font-medium mt-2">Requirements</div>
    <div class="text-sm text-olive mt-0.5">Scope & prioritize</div>
  </div>
  <div class="text-stone text-lg mt-1 px-1">→</div>
  <div class="flex-1 text-center">
    <span class="section-num">02</span>
    <div class="text-sm font-medium mt-2">Development</div>
    <div class="text-sm text-olive mt-0.5">Build & test</div>
  </div>
  <div class="text-stone text-lg mt-1 px-1">→</div>
  <div class="flex-1 text-center">
    <span class="section-num">03</span>
    <div class="text-sm font-medium mt-2">Deploy</div>
    <div class="text-sm text-olive mt-0.5">Ship & monitor</div>
  </div>
</div>
```

### Hierarchy tree (nested structure)

For system architecture, module breakdown, org charts. Nested `border-l` lines
create the tree trunk.

```html
<div class="space-y-3">
  <div class="font-medium text-base text-near-black">API Gateway</div>
  <div class="pl-5 border-l-2 border-brand space-y-2.5">
    <div>
      <div class="text-sm font-medium text-dark-warm">Auth Service</div>
      <div class="text-sm text-olive">JWT validation, OAuth2</div>
    </div>
    <div>
      <div class="text-sm font-medium text-dark-warm">User Service</div>
      <div class="pl-5 border-l border-border-soft mt-1.5 space-y-1.5">
        <div class="text-sm text-olive">Profile module</div>
        <div class="text-sm text-olive">Preferences module</div>
      </div>
    </div>
    <div>
      <div class="text-sm font-medium text-dark-warm">Payment Service</div>
    </div>
  </div>
</div>
```

### Comparison grid (side-by-side options)

For approach evaluation, A-vs-B decisions. Combines `.card`, `.tag`, `.dash`
list, and semantic colors.

```html
<div class="grid grid-cols-2 gap-5">
  <div class="card">
    <div class="flex items-baseline gap-2 mb-3">
      <span class="tag">A</span>
      <h3 class="font-medium text-xl">Option A</h3>
    </div>
    <p class="text-dark-warm mb-3">Short description.</p>
    <div class="grid grid-cols-2 gap-3">
      <div>
        <div class="eyebrow-muted mb-1">Pros</div>
        <ul class="dash"><li class="text-success">Fast setup</li></ul>
      </div>
      <div>
        <div class="eyebrow-muted mb-1">Cons</div>
        <ul class="dash"><li class="text-danger">Limited scale</li></ul>
      </div>
    </div>
  </div>
  <div class="card">
    <div class="flex items-baseline gap-2 mb-3">
      <span class="tag">B</span>
      <h3 class="font-medium text-xl">Option B</h3>
    </div>
    <p class="text-dark-warm mb-3">Short description.</p>
    <div class="grid grid-cols-2 gap-3">
      <div>
        <div class="eyebrow-muted mb-1">Pros</div>
        <ul class="dash"><li class="text-success">Scalable</li></ul>
      </div>
      <div>
        <div class="eyebrow-muted mb-1">Cons</div>
        <ul class="dash"><li class="text-danger">Complex setup</li></ul>
      </div>
    </div>
  </div>
</div>
```

### Tabs

```html
<div class="flex gap-0 border-b border-dotted border-border mb-8">
  <div class="tab px-4.5 py-2.5 text-sm font-medium text-near-black cursor-pointer -mb-px border-b-2 border-brand">Active</div>
  <div class="tab px-4.5 py-2.5 text-sm font-medium text-stone cursor-pointer -mb-px border-b-2 border-transparent hover:text-near-black">Inactive</div>
</div>
```

### Sticky toolbar

```html
<div class="sticky top-0 z-5 bg-parchment flex items-center gap-3.5 py-3.5 mb-3.5 border-b border-dotted border-border">
  <div class="font-mono text-sm text-dark-warm">Summary text</div>
  <div class="flex-1"></div>
  <button class="btn-ghost">Reset</button>
  <button class="btn-primary">Export</button>
</div>
```

### Table (utility-based)

Prefer `.kami-table` class for most cases. Use raw utilities only for highly custom layouts:

```html
<table class="w-full border-collapse text-sm">
  <thead>
    <tr>
      <th class="text-left font-medium text-dark-warm px-3 py-2.5 border-b border-border bg-parchment">Header</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="px-3 py-2.5 border-b border-border-soft align-top">Cell</td>
    </tr>
  </tbody>
</table>
```

---

## The ten design invariants

These rules are non-negotiable. Every HTML file must follow them:

1. **Page background is `parchment` (`#f5f4ed`)** — never pure white for the page
2. **All grays are warm** — yellow-brown undertone (R >= G >= B). Never cool/blue grays
3. **Single accent: `brand` (`#1B365D`)** — ink blue is the sole chromatic accent
4. **Serif-led typography** — sans = serif (TsangerJinKai02). Mono only for code/labels
5. **No bold, no italic** — max weight is 500 (headings) or 600 (labels). Never 700+ or italic
6. **Subtle shadows only** — whisper shadows with warm rgba, no hard drop shadows
7. **Section titles use left-bar** — `border-l-[2.5px] border-brand pl-2 rounded-l-[1.5px]` signature pattern
8. **Separators are dotted** — use `border-dotted border-border` not solid lines for visual division
9. **Numbers use tabular-nums** — `font-variant-numeric: tabular-nums` on all numeric displays
10. **Tailwind utility-first** — use Tailwind classes, semantic CSS for repeated patterns
