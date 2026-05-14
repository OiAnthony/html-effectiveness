# Document Categories

10 categories of HTML artifacts. Each serves a different purpose and has its own
layout patterns.

---

## 1. Exploration & Planning

**When**: User needs to compare approaches, evaluate options, plan implementation.

**Layout**: Side-by-side cards or columns. Each option gets equal visual weight.
Include a recommendation section at the bottom.

**Information flow** (top to bottom):
1. `.prompt-box` — show the prompt that triggered this exploration
2. Metric strip — 3-4 summary dimensions (complexity, risk, effort, bundle size)
3. Grid of equal-weight comparison cards (2-4 columns)
4. Inside each card: title → one-paragraph description → code sample → pro/con table → `.chip` indicators
5. `.callout-brand` recommendation with reasoning

The reader should be able to pick an option by scanning the grid without
reading every line. Pro/con tables and chips provide the at-a-glance signal;
the recommendation callout at the end anchors the decision.

**Key components**:
- `.prompt-box` with `.prompt-label`
- Grid of comparison cards (2-4 columns)
- Pro/con tables (two-column grid inside each card)
- `.chip` indicator strip per card (bundle size, testability, reuse)
- `.callout-brand` recommendation callout with reasoning

**Example filenames**: `auth-approaches-exploration.html`, `migration-plan.html`

---

## 2. Code Review

**When**: PR review, annotated diffs, code walkthrough.

**Layout**: Diff view with annotation bubbles. File tabs at top.

**Information flow**:
1. Header — PR title, branch, author
2. Metric strip — files changed, additions, deletions, findings by severity
3. File tab bar (sticky) — one tab per changed file
4. Per-file: annotated diff with margin bubbles color-coded by severity
5. Summary assessment — overall verdict + key concerns

**Key components**:
- File tab bar (sticky)
- Diff grid: line number | +/- marker | code
- Annotation bubbles (positioned next to relevant lines)
- Summary section with overall assessment
- Statistics strip (files changed, additions, deletions)

**Colors**:
- Additions: `rgba(120,140,93,0.15)` background
- Deletions: `rgba(176,74,63,0.15)` background
- Line numbers: `var(--gray-500)` on dark code background

**Example filenames**: `pr-42-review.html`, `auth-module-walkthrough.html`

---

## 3. Design System

**When**: Show design tokens, component variants, style guide.

**Layout**: Vertical sections — Color, Typography, Spacing, Components.

**Key components**:
- Swatch grids with hex values and token names
- Typography scale (specimen + metadata)
- Spacing ruler visualization
- Component stages (buttons, inputs, badges in context)

**Example filenames**: `design-system.html`, `component-variants.html`

---

## 4. Prototype

**When**: Demonstrate animation, interaction, or UI behavior.

**Layout**: Live preview area with control panel.

**Information flow**:
1. Header — what is being prototyped and why
2. Two-column bench: Stage (preview pane) + Panel (controls)
3. Stage — the live prototype with a "click to toggle" hint
4. Panel — labeled controls (sliders, buttons, presets) that modify CSS
   custom properties via `setProperty()` for instant feedback
5. Below the bench: keyframe timeline showing timing of each animation phase
6. Copy-paste code snippet — the CSS/JS the user takes back to their codebase

The reader should *feel* the interaction before reading any code.

**Key components**:
- Preview pane (the thing being prototyped)
- Control panel: sliders, buttons, dropdowns
- Parameter display showing current values
- Keyframe timeline strip
- Code snippet showing how to implement

**JavaScript**: Use `requestAnimationFrame` for animations, CSS custom properties
for live-tweaking values via controls.

**Example filenames**: `easing-sandbox.html`, `transition-prototype.html`

---

## 5. Illustration & Diagram

**When**: Architecture diagram, flowchart, data-flow visualization, concept
illustration for a blog post or doc page.

**Layout**: Large SVG centered on page, with optional legend or annotations.

**Information flow**:
1. Header — what this diagram depicts
2. `<figure>` with inline `<svg>` inside a `.card` container (rounded, bordered)
3. `<figcaption>` below — one-sentence description of what the reader is seeing
4. Optional: legend strip explaining color coding and line styles
5. Optional: click-to-reveal detail panel on nodes for deeper info

The diagram should be self-explanatory at a glance. Use position and color
to show hierarchy; use annotations (`<text>`) to label non-obvious elements.
Solid lines for synchronous / primary flows, dashed for async / optional.

**Key components**:
- `<defs>` with reusable arrow `<marker>` definitions
- `<rect rx="10">` box nodes with centered `<text>` (title + subtitle)
- Dark-filled rects for databases / storage, light for services
- `<path marker-end>` connections (solid = sync, dashed = async)
- Annotation `<text>` in stone color near relevant elements
- `<figure>` + `<figcaption>` wrapper

**SVG style**: Strokes 1.5-2px. Rounded corners `rx="10"` on all rects.
Use Kami hex values directly for fills and strokes (CSS custom properties
are unreliable inside inline SVG). Fonts: match page mono/sans stacks.
See the "Inline SVG diagrams" recipe in SKILL.md for the full skeleton.

**Example filenames**: `system-architecture.html`, `data-flow-diagram.html`

---

## 6. Slide Deck

**When**: Present information to an audience, screen by screen.

**Layout**: Full-viewport slides with CSS scroll-snap.

**Key components**:
- Title slide: Display heading + subtitle
- Content slides: Heading + key points (not paragraphs)
- Slide counter (bottom-right)
- Arrow-key and click navigation

**Rules**:
- Max 6-8 words per bullet
- Max 4-5 bullets per slide
- One idea per slide
- Large type (28px+ for body)

**Example filenames**: `q4-review-deck.html`, `architecture-proposal.html`

---

## 7. Research & Explainer

**When**: Explain a concept, document findings, feature deep-dive.

**Layout**: Main content column + optional sticky sidebar.

**Information flow**:
1. Header + lead paragraph — the one-sentence answer
2. Main column: progressive explanation with inline live demos
3. Optional sticky `<aside>` — glossary / key terms / table of contents
4. Hover-linked terms: `<span class="term">` in body highlights the matching
   glossary entry in the sidebar (see interaction recipes in SKILL.md)
5. Comparison table — the "vs" moment that crystallizes the concept
6. Closing section — where you will meet this / when to use it

The sidebar glossary turns a linear read into a spatial reference.
Terms in the body text are underlined with dotted borders; hovering
highlights the glossary entry, anchoring unfamiliar vocabulary without
interrupting the reading flow.

**Key components**:
- Sticky `<aside>` glossary with `<dl>` terms
- Hover-linked `.term` spans in body text
- Collapsible `<details>` for supplementary info
- Inline live demos (SVG, interactive controls)
- Comparison tables

**Example filenames**: `react-server-components-explainer.html`, `caching-strategies-research.html`

---

## 8. Report

**When**: Status update, incident timeline, weekly summary.

**Layout**: Metric strip at top, then chronological or categorized sections.

**Key components**:
- 3-4 metric cards in a grid (number + label)
- Status badges (on-track, at-risk, blocked)
- Timeline entries with timestamps
- Section cards with status indicators

**Metric card style**:
- Big serif number in `--clay` color
- Small label below in `--gray-500`

**Example filenames**: `sprint-14-status.html`, `incident-2024-03-report.html`

---

## 9. Custom Editor

**When**: User needs a throwaway tool to manipulate data — triage tickets, toggle
feature flags, tune prompts, debug regex.

**Layout**: Toolbar + main editing area + export button.

**Information flow** (closed-loop workflow):
1. Header — what data is being edited and the goal
2. Sticky toolbar — live summary counts + filter pill + reset + **export button**
3. Main editing area — cards, board columns, or form fields
4. User manipulates data → toolbar counts update in real-time
5. Export button → copies structured output (Markdown / JSON / prompt) to
   clipboard → user pastes back into agent for next iteration

The export is the whole point. Design the export format first (what will the
agent or commit need?), then build the editor around it.

**Key components**:
- Sticky toolbar with summary stats and action buttons
- Main area: cards, board columns, or form fields
- Filter/search controls with dim-not-hide behavior (non-matching items
  go to `opacity: 0.25`, preserving spatial context)
- **Export button** (MANDATORY) — copies current state as JSON/Markdown/CSV

**Interactivity**:
- Drag and drop for reordering or categorizing
- Inline editing (contenteditable or input fields)
- Real-time filtering and search (tag click → filter → clear pill)
- Visual feedback on state changes

**Rules**:
- Data-driven: define `DATA` array at top, render from it
- All state changes update the data model, then re-render
- Export serializes the data model, not the DOM

**Example filenames**: `cycle-14-triage.html`, `feature-flags-editor.html`

---

## 10. Changelog

**When**: Release notes, version history, product updates, migration guides.

**Layout**: Centered version header + categorized entry lists with filter buttons.

**Key components**:
- `.version-header` — Project name, version number, tagline, date
- Filter bar — Toggle visibility by category (Breaking / Features / Fixes)
- `.h2-bar` sections per category
- Numbered change lists (`ol.changes`) with `.tag` / `.tag-breaking` markers
- `.callout-light` acknowledgments block
- `.doc-footer`

**Interactivity**:
- Category filter buttons (JS show/hide by `data-type`)
- All categories visible by default

**Rules**:
- Each entry is one sentence — concise and actionable
- Breaking changes always come first and use `.tag-breaking`
- Version number is the visual anchor (largest text element)

**Example filenames**: `v2.1-changelog.html`, `api-migration-notes.html`
