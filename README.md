<p align="center">
    <img src="./docs/banner.png" alt="geg-toanki Banner" width="200">
</p>

<h1 align="center">geg-toanki</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-0062AF?style=for-the-badge&logo=python&logoColor=f6f6f6" />
  <img src="https://img.shields.io/badge/Gemini-0062AF?style=for-the-badge&logo=googlegemini&logoColor=f6f6f6" />
  <img src="https://img.shields.io/badge/Typer-0062AF?style=for-the-badge&logo=python&logoColor=f6f6f6" />
  <img src="https://img.shields.io/badge/uv-0062AF?style=for-the-badge&logo=uv&logoColor=f6f6f6" />
</p>

<p align="center">
  CLI tool for turning Markdown materials into flashcards and sending them directly to Anki, with support for automatic AI-powered card generation.
</p>

## Features

* [x] Support for `.pdf`, `.txt`, and `.md` files
* [x] Convert input files to Markdown using `geg-tomd`
* [x] Automatic flashcard generation with Gemini
* [x] Create decks and subdecks in Anki
* [x] Send cards via AnkiConnect
* [x] Organize cards based on directory structure

## Upcoming Features

* [ ] **Temporary directory management** — store summaries in a temporary directory and copy them to the output directory when requested.
* [ ] **Flashcard validation** — filter out vague, duplicate, or incomplete answers.
* [ ] **Chunking** — process large amounts of content in smaller chunks before generation.
* [ ] **Terminal preview** — preview cards before sending them to Anki.
* [ ] **`.apkg` export** — generate deck packages directly.
* [ ] **Tags and customization** — add tags and per-subject/topic settings.
* [ ] **Error handling and logging** — improve diagnostics and failure messages.
* [ ] **Automated tests** — cover parsing, generation, and Anki integration.

## Prerequisites

Before using the project, make sure you have:

* Python 3.14+
* `uv` installed
* Anki installed locally
* AnkiConnect running
* A Gemini API key configured in `GEMINI_API_KEY`

The application also depends on the local `geg-tomd` package, which is automatically added to `pyproject.toml`.

## Installation

```bash
git clone https://github.com/gabrielescorelguerra/geg-toanki.git
cd geg-toanki

uv sync
```

Configure the environment variables before running the CLI:

```bash
export GEMINI_API_KEY="your_api_key"
export ANKI_CONNECT_URL="http://localhost:8765"
```

## Usage

### View Help

```bash
uv run geg-toanki --help
```

### Generate Cards from a File

```bash
uv run geg-toanki create ./material.pdf --deck "Biology" --subdecks
```

### Generate Intermediate Markdown Files

```bash
uv run geg-toanki create ./material.pdf --deck "History" --generate-md
```

### Options

| Option                | Description                                                     |
| --------------------- | --------------------------------------------------------------- |
| `-d`, `--deck`        | Name of the main Anki deck                                      |
| `-s`, `--subdecks`    | Create subdecks based on the directory structure                |
| `-m`, `--generate-md` | Generate intermediate Markdown files in the temporary directory |
| `input_path_str`      | Path to the input file (PDF, TXT, or MD)                        |

## Project Workflow

1. The input file is processed and converted to Markdown.
2. The content is read from the `.geg/toanki/temp` temporary directory.
3. Each Markdown file is sent to the Gemini model.
4. The model returns a JSON object containing structured flashcards.
5. The cards are sent to Anki via AnkiConnect.

## Notes

* The project uses `geg-tomd` as a local dependency to convert content to Markdown before generating flashcards.
* Anki integration requires AnkiConnect to be accessible at the configured endpoint.
* The current command is designed for study workflows and generating flashcards from academic or reference materials.
