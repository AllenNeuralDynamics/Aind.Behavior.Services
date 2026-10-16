"""MkDocs build hooks for generating dynamic documentation assets.

Runs on every ``mkdocs build`` / ``mkdocs serve``:

* copies ``README.md`` into ``docs/index.md`` (the site home page);
* exports the framework's JSON schemas into ``docs/schema/``;
* renders each JSON schema as a Markdown page under ``docs/schema/``
  and injects a "JSON Schemas" section into the navigation.
"""

import logging
from pathlib import Path
from typing import Any

log = logging.getLogger("mkdocs.hooks")

REPO_ROOT = Path(__file__).parent.parent
DOCS_DIR = REPO_ROOT / "docs"
SCHEMA_DOCS_DIR = DOCS_DIR / "schema"
SCHEMAS_LABEL = "JSON Schemas"


def on_pre_build(config: dict[str, Any], **kwargs) -> None:
    """MkDocs pre-build hook."""
    _copy_readme()
    _generate_schemas()
    schema_nav = _render_schema_pages()
    if schema_nav:
        _inject_nav(config, schema_nav)


def _copy_readme() -> None:
    readme = REPO_ROOT / "README.md"
    index = DOCS_DIR / "index.md"
    if not readme.exists():
        log.warning("README.md not found, skipping index copy")
        return
    text = readme.read_text(encoding="utf-8")
    # The knowledge/ tree is intentionally excluded from the rendered site and
    # surfaced on GitHub instead. Rewrite the README's repo-relative links to it
    # into absolute GitHub URLs so they resolve on the site (and still on GitHub).
    gh_blob = "https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/"
    text = text.replace("](docs/knowledge/", f"]({gh_blob}")
    index.write_text(text, encoding="utf-8")
    log.info("Copied README.md -> docs/index.md")


def _generate_schemas() -> None:
    """Export the schemas of every module in the package into ``docs/schema/``."""
    try:
        from bonsai.sgen.cli import main as sgen_main

        SCHEMA_DOCS_DIR.mkdir(parents=True, exist_ok=True)
        sgen_main(["export", "aind_behavior_services", "--allow-local-types", "-o", str(SCHEMA_DOCS_DIR)])
    except Exception as e:  # noqa: BLE001  # pragma: no cover - build-time best effort
        log.warning(f"Skipping schema export: {e}")


def _render_schema_pages() -> list[dict[str, str]]:
    """Render each schema/*.json as a Markdown page and return nav entries.

    Follows the vr-foraging convention: a download button plus the raw JSON in a
    collapsible block. The JSON is inlined into the page (rather than pulled via a
    ``--8<--`` snippet) so rendering does not depend on the build's working directory.
    """
    if not SCHEMA_DOCS_DIR.exists():
        log.warning("docs/schema directory not found, skipping schema pages")
        return []

    nav_entries: list[dict[str, str]] = []
    for json_file in sorted(SCHEMA_DOCS_DIR.glob("*.json")):
        stem = json_file.stem
        title = stem.rpartition(".")[2]

        raw = json_file.read_text(encoding="utf-8")
        indented = "\n".join(f"    {line}" if line else "" for line in raw.splitlines())
        page = (
            f"# {title}\n\n"
            "Generated from the Pydantic models in `aind_behavior_services` and used to "
            "generate the C# serializers via `Bonsai.Sgen`.\n\n"
            f"[:material-download: Download `{json_file.name}`]({json_file.name}){{ .md-button }}\n\n"
            '??? note "Full schema (expand to view)"\n\n'
            f"    ```json\n{indented}\n    ```\n"
        )
        (SCHEMA_DOCS_DIR / f"{stem}.md").write_text(page, encoding="utf-8")

        nav_entries.append({title: f"schema/{stem}.md"})
        log.info(f"Rendered schema page -> schema/{stem}.md")

    return nav_entries


def _inject_nav(config: dict[str, Any], schema_nav: list[dict[str, str]]) -> None:
    """Append (or replace) the JSON Schemas section in the MkDocs nav."""
    nav: list[Any] = config.get("nav") or []
    nav = [item for item in nav if not (isinstance(item, dict) and SCHEMAS_LABEL in item)]
    nav.append({SCHEMAS_LABEL: schema_nav})
    config["nav"] = nav
