# Contributing to Instagram Agent (Codex Edition)

We welcome contributions to improve the skills, formulas, and tooling in this repository.

## Contribution Guidelines

1. **Preserve Human-in-the-Loop Boundaries**:
   - Do not add features that automate publishing, automated scraping, or bulk DMing. All workflows must terminate in a copy-ready block for the user to review.
2. **Zero Dependency Tooling**:
   - All tools in `scripts/` must remain runnable using Python's standard library alone. Do not introduce mandatory third-party dependencies.
3. **Updating Hook Formulas (`references/hooks.json`)**:
   - Each formula requires an `id`, `name`, `template`, `example`, `on_screen`, `best_for`, `trap`, and a robust `match` regex.
   - Formulas must be tested against real conversational speech.
4. **Updating the Slop Lexicon (`references/slop.json`)**:
   - When adding stock AI phrases, provide plain-English replacements that preserve grammar and capitalization.
5. **Testing**:
   - Any script modification must be covered by automated tests in `tests/`.
   - Ensure the full test suite passes before submitting changes:
     ```bash
     python3 -m unittest discover tests
     ```
