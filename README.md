# Content Moderation Queue

Purpose
- Rank moderation items and highlight high-risk content.

What this project does
- Loads structured data for flag records
- Validates records against rules and allowed categories
- Computes summary metrics and a ranked highlight
- Produces a plain-text report for quick review

Structure
- `config.json`: domain labels and categories
- `data/sample.json`: example dataset and expected results
- `python/`: Python CLI and library
- `js/`: Node.js CLI and library
- `docs/design.md`: design notes and extension ideas
- `.github/workflows/ci.yml`: tests for Python and JS

Quickstart
- Python: `python python/app.py data/sample.json`
- Node: `node js/app.js data/sample.json`

Tests
- Python: `python -m unittest discover -s python/tests -p "test_*.py"`
- Node: `node js/tests/run.js`
