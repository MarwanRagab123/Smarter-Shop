<!-- prettier-ignore -->
# Smarter Shop 🚀

![python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![tests](https://img.shields.io/badge/tests-unittest-brightgreen.svg)
![license](https://img.shields.io/badge/license-MIT-lightgrey.svg)

Smarter Shop is a small, well-organized Python demo app that shows how to structure Agents, Tasks and utility tools for lightweight procurement and price-comparison workflows.

## Table of Contents

- [Quick links](#quick-links)
- [What this repo contains](#what-this-repo-contains)
- [Architecture (big picture)](#architecture-big-picture)
- [Quickstart (Windows cmd)](#quickstart-windows-cmd)
- [Run the app](#run-the-app)
- [Run tests](#run-tests)
- [Useful locations & patterns](#useful-locations--patterns)
- [Contributing](#contributing)
- [License](#license)

## Quick links

- Code: `main.py`, `src/Agents/`, `src/Tasks/`, `tool/`
- Tests: `tests/test_app.py`
- Data samples: `Data/key_word_task_output.json`

## What this repo contains

High-level layout (top-level):

```
my-python-app/
├─ main.py                # entry point (light orchestration)
├─ src/                   # core packages
│  ├─ Agents/             # agent implementations (scrapers, extractors)
│  └─ Tasks/              # small Task classes that Agents use
├─ tool/                  # small tools and adapters used by agents
├─ Data/                  # sample outputs and fixtures
└─ tests/                 # unit tests (unittest)
```

## Architecture (big picture)

- Agents (in `src/Agents`) implement domain behavior. Example files: `extract_key_word.py`, `procurement_report_author_agent.py`.
- Tasks (in `src/Tasks`) encapsulate a single unit of work and are lightweight, focused classes used by agents (see `key_word_task.py`).
- Tools (in `tool/`) are small, procedural helpers for web scraping and search adapters; they are imported by Agents.
- `main.py` orchestrates execution (light CLI) and composes Agents + Tasks for simple runs.

Design intention: keep Agents thin and testable by moving non-business logic into `tool/` helpers and small `Task` classes. This keeps side-effects (I/O, scraping) in isolated modules.

## Quickstart (Windows cmd)

Open a Windows command prompt (cmd.exe) in the repository root.

1. Create a virtual environment (optional but recommended):

```bat
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```bat
pip install -r requirements.txt
```

3. Run the app (example):

```bat
python main.py
```

## Run the app

The project is lightweight; `main.py` is the simplest entry point for demo runs. For more targeted checks, run individual Agents inside a Python REPL or small runner script.

Example: run a specific module directly

```bat
python -m src.Agents.extract_key_word
```

## Run tests

Unit tests use Python's `unittest`. To run all tests:

```bat
python -m unittest discover -s tests
```

To run a single test file:

```bat
python -m unittest tests.test_app
```

## Useful locations & patterns (project-specific)

- Agent → Task pattern: Agents are in `src/Agents/` and use Task classes in `src/Tasks/`. See `src/Agents/extract_key_word.py` and `src/Tasks/key_word_task.py` for the pattern: Agents orchestrate calls, Tasks hold small processing logic.
- Tools: small scripts under `tool/` expose procedural functions (for example `web_scarping_tool1.py`) and are imported directly by Agents.
- Data fixtures live in `Data/` and are safe to reference in tests (example: `Data/key_word_task_output.json`).
- Tests: keep tests in `tests/` and use `unittest` discovery. Tests reference modules by package path when needed.

## Contributing

1. Fork the repo and create a branch for your change.
2. Keep changes focused and add tests for new logic.
3. Run `python -m unittest discover -s tests` before opening a PR.

If you add external API keys or secrets, add them to `.env` and do not commit them.

## License

MIT — see the `LICENSE` file for details.

---
