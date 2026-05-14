"""Shared constants and helpers for html-effectiveness scripts."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "assets" / "templates"
COMPONENTS_CSS = ROOT / "assets" / "components.css"
OUTPUT_DIR = Path.cwd()

TEMPLATE_REGISTRY: dict[str, dict] = {
    "exploration": {
        "source": "exploration.html",
        "description": "Compare options with pros/cons and a recommendation",
        "default_eyebrow": "Exploration",
        "default_subtitle": "",
    },
    "report": {
        "source": "report.html",
        "description": "Metrics dashboard with timeline and sections",
        "default_eyebrow": "Report",
        "default_subtitle": "",
    },
    "code-review": {
        "source": "code-review.html",
        "description": "Diff viewer with annotations and file tabs",
        "default_eyebrow": "Code Review",
        "default_subtitle": "",
    },
    "deck": {
        "source": "deck.html",
        "description": "Full-screen slide deck with keyboard navigation",
        "default_eyebrow": "Presentation",
        "default_subtitle": "",
    },
    "editor": {
        "source": "editor.html",
        "description": "Kanban board with drag-and-drop and export",
        "default_eyebrow": "Editor",
        "default_subtitle": "",
    },
    "research": {
        "source": "research.html",
        "description": "Tabbed research document with collapsible sections",
        "default_eyebrow": "Research",
        "default_subtitle": "",
    },
    "changelog": {
        "source": "changelog.html",
        "description": "Version changelog with categorized entries and filters",
        "default_eyebrow": "Changelog",
        "default_subtitle": "",
    },
}


def inject_components_css(html: str) -> str:
    """Inject semantic component classes into the tailwindcss style block."""
    if not COMPONENTS_CSS.exists():
        return html
    css = COMPONENTS_CSS.read_text()
    marker = "</style>\n</head>"
    return html.replace(marker, f"\n{css}</style>\n</head>", 1)


def slugify(text: str) -> str:
    """Convert text to a filename-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:60].rstrip("-")


def resolve_output_path(explicit: str | None, template: str, title: str) -> Path:
    """Determine the output file path."""
    if explicit:
        return Path(explicit)
    slug = slugify(title) if title != "Untitled" else template
    return OUTPUT_DIR / f"{slug}.html"
