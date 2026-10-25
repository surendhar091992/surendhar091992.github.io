#!/usr/bin/env python3
"""Convert one BibTeX file into Academic Pages publication Markdown files.

Place this script and pub_list_own.bib in markdown_generator/.
Install the dependency: python -m pip install pybtex
Run from any directory: python markdown_generator/bib_to_pubby_own.py
"""

from datetime import date
import json
from pathlib import Path
import re
from urllib.parse import quote_plus

from pybtex.database.input import bibtex


# Paths are relative to this script, so the command works from any directory.
SCRIPT_DIR = Path(__file__).resolve().parent
BIB_FILE = SCRIPT_DIR / "pub_list_own.bib"
OUTPUT_DIR = SCRIPT_DIR.parent / "_publications"


def clean(text):
    """Remove simple BibTeX capitalization braces (not a full LaTeX parser)."""
    return str(text).replace("{", "").replace("}", "").replace(r"\&", "&").strip()


def yaml_string(text):
    """JSON strings are valid YAML double-quoted scalar strings."""
    return json.dumps(str(text), ensure_ascii=False)


def publication_date(fields):
    year_string = clean(fields["year"])
    if not re.fullmatch(r"\d{4}", year_string):
        raise ValueError(f"Invalid year: {year_string}")

    month_string = clean(fields.get("month", "1")).lower().strip(". ")
    month_names = {
        "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
        "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
    }
    month = int(month_string) if month_string.isdigit() else month_names.get(month_string[:3], 1)
    day_string = clean(fields.get("day", "1"))
    day = int(day_string) if day_string.isdigit() else 1

    try:
        return date(int(year_string), month, day).isoformat()
    except ValueError:
        print(f"  WARNING: Invalid month/day for {year_string}; using January 1.")
        return f"{year_string}-01-01"


def paper_link(fields):
    url = clean(fields.get("url", ""))
    if url:
        return url

    doi = clean(fields.get("doi", ""))
    if doi:
        doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.I)
        return "https://doi.org/" + doi

    return ""


def create_markdown(bib_key, entry):
    fields = entry.fields
    kind = entry.type.lower()
    if kind not in {"article", "inproceedings"}:
        print(f"SKIPPED {bib_key}: unsupported BibTeX type @{kind}")
        return None

    if "title" not in fields or "year" not in fields:
        print(f"SKIPPED {bib_key}: missing title or year")
        return None

    title = clean(fields["title"])
    pub_date = publication_date(fields)
    note = clean(fields.get("note", ""))
    abstract = clean(fields.get("abstract", ""))

    if kind == "article":
        category = "manuscripts"  # Academic Pages default: Journal Articles
        venue = clean(fields.get("journal", "")) or note.strip("() ") or "Manuscript"
    else:
        category = "conferences"  # Academic Pages default: Conference Papers
        # Handles the IFAC-PapersOnLine entry that has journal but no booktitle.
        venue = clean(fields.get("booktitle", "")) or clean(fields.get("journal", ""))
        venue = venue or "Conference paper"
        if note and note.lower().startswith(("10th ifac", "conference")):
            venue += f" ({note})"

    slug = re.sub(r"[^a-z0-9_-]+", "-", bib_key.lower()).strip("-")
    if not slug:
        print(f"SKIPPED {bib_key}: invalid BibTeX key")
        return None

    url = paper_link(fields)

    lines = [
        "---",
        f"title: {yaml_string(title)}",
        "collection: publications",
        f"category: {category}",
        f"permalink: /publication/{slug}/",
        f"date: {pub_date}",
        f"venue: {yaml_string(venue)}",
        "generated_by: pubsFromBib.py",
    ]
    if note:
        lines.append(f"excerpt: {yaml_string(note)}")
    if url:
        lines.append(f"paperurl: {yaml_string(url)}")
    lines.extend(["---", ""])

    # Show an Abstract section on the individual publication page only
    # when a non-empty abstract exists in the BibTeX entry.
    if abstract:
        lines.extend(["## Abstract", "", abstract, ""])

    if note:
        lines.extend([note, ""])
    if url:
        lines.append(f'[Read paper]({url}){{:target="_blank"}}')
    elif not note:
        scholar_url = "https://scholar.google.com/scholar?q=" + quote_plus(title)
        lines.append(f'[Search on Google Scholar]({scholar_url}){{:target="_blank"}}')

    return f"bib-{slug}.md", "\n".join(lines) + "\n"


def main():
    if not BIB_FILE.is_file():
        raise SystemExit(f"ERROR: Cannot find BibTeX file: {BIB_FILE}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data = bibtex.Parser().parse_file(str(BIB_FILE))
    written = set()

    for bib_key, entry in data.entries.items():
        try:
            result = create_markdown(bib_key, entry)
            if result is None:
                continue
            filename, content = result
            (OUTPUT_DIR / filename).write_text(content, encoding="utf-8")
            written.add(filename)
            print(f"GENERATED {bib_key} -> {filename}")
        except (ValueError, KeyError) as error:
            print(f"SKIPPED {bib_key}: {error}")

    # Remove only stale files previously created by THIS script.
    # Manually written Markdown files and template examples are untouched.
    for old_file in OUTPUT_DIR.glob("bib-*.md"):
        if old_file.name not in written:
            if "generated_by: pubsFromBib.py" in old_file.read_text(encoding="utf-8"):
                old_file.unlink()
                print(f"REMOVED old generated file: {old_file.name}")

    print(f"\nDone: {len(written)} publication(s) in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
























# #!/usr/bin/env python3
# """Convert one BibTeX file into Academic Pages publication Markdown files.

# Place this script and pub_list_own.bib in markdown_generator/.
# Install the dependency: python -m pip install pybtex
# Run from any directory: python markdown_generator/pubsFromBib.py
# """

# from datetime import date
# from html import escape
# import json
# from pathlib import Path
# import re
# from urllib.parse import quote_plus

# from pybtex.database.input import bibtex


# # Paths are relative to this script, so the command works from any directory.
# SCRIPT_DIR = Path(__file__).resolve().parent
# BIB_FILE = SCRIPT_DIR / "pub_list_own.bib"
# OUTPUT_DIR = SCRIPT_DIR.parent / "_publications"


# def clean(text):
#     """Remove simple BibTeX capitalization braces (not a full LaTeX parser)."""
#     return str(text).replace("{", "").replace("}", "").replace(r"\&", "&").strip()


# def yaml_string(text):
#     """JSON strings are valid YAML double-quoted scalar strings."""
#     return json.dumps(str(text), ensure_ascii=False)


# def format_authors(entry):
#     names = []
#     for person in entry.persons.get("author", []):
#         parts = (
#             list(person.first_names)
#             + list(person.middle_names)
#             + list(person.prelast_names)
#             + list(person.last_names)
#             + list(person.lineage_names)
#         )
#         names.append(clean(" ".join(parts)))
#     return ", ".join(names) or "Unknown authors"


# def publication_date(fields):
#     year_string = clean(fields["year"])
#     if not re.fullmatch(r"\d{4}", year_string):
#         raise ValueError(f"Invalid year: {year_string}")

#     month_string = clean(fields.get("month", "1")).lower().strip(". ")
#     month_names = {
#         "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
#         "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
#     }
#     month = int(month_string) if month_string.isdigit() else month_names.get(month_string[:3], 1)
#     day_string = clean(fields.get("day", "1"))
#     day = int(day_string) if day_string.isdigit() else 1

#     try:
#         return date(int(year_string), month, day).isoformat()
#     except ValueError:
#         print(f"  WARNING: Invalid month/day for {year_string}; using January 1.")
#         return f"{year_string}-01-01"


# def paper_link(fields):
#     url = clean(fields.get("url", ""))
#     if url:
#         return url

#     doi = clean(fields.get("doi", ""))
#     if doi:
#         doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.I)
#         return "https://doi.org/" + doi

#     return ""


# def create_markdown(bib_key, entry):
#     fields = entry.fields
#     kind = entry.type.lower()
#     if kind not in {"article", "inproceedings"}:
#         print(f"SKIPPED {bib_key}: unsupported BibTeX type @{kind}")
#         return None

#     if "title" not in fields or "year" not in fields:
#         print(f"SKIPPED {bib_key}: missing title or year")
#         return None

#     title = clean(fields["title"])
#     pub_date = publication_date(fields)
#     authors = format_authors(entry)
#     note = clean(fields.get("note", ""))

#     if kind == "article":
#         category = "manuscripts"  # Academic Pages default: Journal Articles
#         venue = clean(fields.get("journal", "")) or note.strip("() ") or "Manuscript"
#     else:
#         category = "conferences"  # Academic Pages default: Conference Papers
#         # Handles the IFAC-PapersOnLine entry that has journal but no booktitle.
#         venue = clean(fields.get("booktitle", "")) or clean(fields.get("journal", ""))
#         venue = venue or "Conference paper"
#         if note and note.lower().startswith(("10th ifac", "conference")):
#             venue += f" ({note})"

#     slug = re.sub(r"[^a-z0-9_-]+", "-", bib_key.lower()).strip("-")
#     if not slug:
#         print(f"SKIPPED {bib_key}: invalid BibTeX key")
#         return None

#     citation = f'{authors}. "{title}." {venue}, {pub_date[:4]}.'
#     url = paper_link(fields)

#     lines = [
#         "---",
#         f"title: {yaml_string(title)}",
#         "collection: publications",
#         f"category: {category}",
#         f"permalink: /publication/{slug}/",
#         f"date: {pub_date}",
#         f"venue: {yaml_string(venue)}",
#         # f"citation: {yaml_string(escape(citation, quote=False))}",
#         "generated_by: pubsFromBib.py",
#     ]
#     if note:
#         lines.append(f"excerpt: {yaml_string(note)}")
#     if url:
#         lines.append(f"paperurl: {yaml_string(url)}")
#     lines.extend(["---", ""])

#     if note:
#         lines.extend([note, ""])
#     if url:
#         lines.append(f'[Read paper]({url}){{:target="_blank"}}')
#     elif not note:
#         scholar_url = "https://scholar.google.com/scholar?q=" + quote_plus(title)
#         lines.append(f'[Search on Google Scholar]({scholar_url}){{:target="_blank"}}')

#     return f"bib-{slug}.md", "\n".join(lines) + "\n"


# def main():
#     if not BIB_FILE.is_file():
#         raise SystemExit(f"ERROR: Cannot find BibTeX file: {BIB_FILE}")

#     OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
#     data = bibtex.Parser().parse_file(str(BIB_FILE))
#     written = set()

#     for bib_key, entry in data.entries.items():
#         try:
#             result = create_markdown(bib_key, entry)
#             if result is None:
#                 continue
#             filename, content = result
#             (OUTPUT_DIR / filename).write_text(content, encoding="utf-8")
#             written.add(filename)
#             print(f"GENERATED {bib_key} -> {filename}")
#         except (ValueError, KeyError) as error:
#             print(f"SKIPPED {bib_key}: {error}")

#     # Remove only stale files previously created by THIS script.
#     # Manually written Markdown files and template examples are untouched.
#     for old_file in OUTPUT_DIR.glob("bib-*.md"):
#         if old_file.name not in written:
#             if "generated_by: pubsFromBib.py" in old_file.read_text(encoding="utf-8"):
#                 old_file.unlink()
#                 print(f"REMOVED old generated file: {old_file.name}")

#     print(f"\nDone: {len(written)} publication(s) in {OUTPUT_DIR}")


# if __name__ == "__main__":
#     main()