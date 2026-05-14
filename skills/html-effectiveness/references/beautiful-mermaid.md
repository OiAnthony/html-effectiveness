# beautiful-mermaid Reference

Zero-dependency Mermaid → SVG renderer. Parses Mermaid DSL and outputs styled
inline SVG with ELK.js layout — no browser runtime, no external fetch at
render time (the ESM module is loaded once).

- Source: <https://github.com/lukilabs/beautiful-mermaid>
- CDN: `https://esm.sh/beautiful-mermaid`

## API

```ts
import { renderMermaidSVG } from 'beautiful-mermaid'

const svg: string = renderMermaidSVG(mermaidSource, {
  bg, fg, accent, muted, surface, border,  // color tokens
  font,        // font family (default: Inter)
  transparent, // true → no background rect
  interactive, // true → hover/tooltip on XY charts
  padding,     // number, px around diagram
})
```

Returns an SVG string (or empty string on parse failure).

## Kami Theme Mapping

| Option    | Kami token  | Hex       | Role                          |
|-----------|-------------|-----------|-------------------------------|
| `bg`      | parchment   | `#f5f4ed` | Diagram canvas                |
| `fg`      | near-black  | `#141413` | Primary text, nodes           |
| `accent`  | brand       | `#1B365D` | Highlighted paths, focal nodes|
| `muted`   | stone       | `#6b6a64` | Edge labels, secondary text   |
| `surface` | ivory       | `#faf9f5` | Node fill                     |
| `border`  | border      | `#e8e6dc` | Node/group strokes            |

## Supported Diagram Types

| Mermaid syntax       | Category  | Use when                                     |
|----------------------|-----------|----------------------------------------------|
| `graph TD` / `LR`   | Flowchart | Flowcharts, decision trees, architecture maps|
| `stateDiagram-v2`   | State     | State machines, lifecycles                   |
| `sequenceDiagram`   | Sequence  | API call flows, actor interactions           |
| `classDiagram`      | Class     | Class relationships, type hierarchies        |
| `erDiagram`         | ER        | Database schemas, entity relationships       |
| `xychart-beta`      | XY Chart  | Bar charts, line charts, trend data          |

## Flowchart Node Shapes

```
A[Rectangle]  B(Rounded)  C{Diamond}  D([Stadium])  E((Circle))
F[[Subroutine]]  G(((Double Circle)))  H{{Hexagon}}
I[(Cylinder)]  J>Flag]  K[/Trapezoid\]  L[\Inverse/]
```

## Flowchart Edge Styles

```
A --> B          solid arrow
A --- B          solid line (no arrow)
A -.-> B         dotted arrow
A -.- B          dotted line
A ==> B          thick arrow
A === B          thick line
A --text--> B    labeled edge
A ---|text|B     labeled line
```

## Key Syntax Notes

- Subgraphs: `subgraph Title ... end`
- Edge labels: `A -->|label| B` or `A --label--> B`
- Text formatting in labels: `**bold**`, `*italic*`
- Node IDs are reusable across edges
- Keep diagrams ≤12 nodes; split larger ones into multiple figures

## Embedding Pattern

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

## Sample Reference

Full syntax coverage with examples:
<https://github.com/lukilabs/beautiful-mermaid/blob/main/samples-data.ts>
