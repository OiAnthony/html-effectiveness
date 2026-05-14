#!/usr/bin/env python3
"""Initialize an HTML artifact from a template."""
from __future__ import annotations

import argparse
import sys

from shared import TEMPLATES, TEMPLATE_REGISTRY, inject_components_css, inject_mermaid_script, resolve_output_path

EPILOG = """\
examples:
  %(prog)s exploration "API Design Options"
  %(prog)s report --title "Q1 Status" --eyebrow "Engineering"
  %(prog)s deck -t "Pitch Deck" -s "Series A" -o ./deck.html
  %(prog)s --list
"""


def fill_template(template: str, replacements: dict[str, str]) -> str:
    """Replace {{PLACEHOLDER}} tokens in template with provided values."""
    result = template
    for key, value in replacements.items():
        result = result.replace("{{" + key + "}}", value)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scaffold an HTML artifact from a template with title/subtitle/eyebrow pre-filled.",
        epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "template",
        nargs="?",
        choices=list(TEMPLATE_REGISTRY.keys()),
        metavar="TEMPLATE",
        help="template name (%(choices)s)",
    )
    parser.add_argument(
        "title_positional",
        nargs="?",
        metavar="TITLE",
        help="document title (positional shorthand for --title)",
    )
    parser.add_argument("--title", "-t", help="document title")
    parser.add_argument("--subtitle", "-s", default="", help="subtitle text")
    parser.add_argument("--eyebrow", "-e", default="", help="eyebrow/category label")
    parser.add_argument("--output", "-o", metavar="PATH", help="output file path (default: output/<slug>.html)")
    parser.add_argument("--list", "-l", action="store_true", help="list available templates and exit")

    args = parser.parse_args()

    if args.list:
        print("Available templates:\n")
        for name, info in TEMPLATE_REGISTRY.items():
            print(f"  {name:<14} {info['description']}")
        print(f"\nTemplates directory: {TEMPLATES}")
        sys.exit(0)

    if not args.template:
        parser.error("template name is required (use --list to see available)")

    title = args.title or args.title_positional or "Untitled"
    info = TEMPLATE_REGISTRY[args.template]
    source = TEMPLATES / info["source"]

    if not source.exists():
        print(f"Error: template file not found: {source}", file=sys.stderr)
        sys.exit(1)

    template_content = source.read_text()

    replacements = {
        "TITLE": title,
        "SUBTITLE": args.subtitle or info.get("default_subtitle", ""),
        "EYEBROW": args.eyebrow or info.get("default_eyebrow", ""),
    }

    html = fill_template(template_content, replacements)
    html = inject_components_css(html)
    html = inject_mermaid_script(html)
    output_path = resolve_output_path(args.output, args.template, title)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    print(f"Created: {output_path}")


if __name__ == "__main__":
    main()
