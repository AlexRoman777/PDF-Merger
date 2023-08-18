# PDF Merger

[![CodeFactor](https://www.codefactor.io/repository/github/alexroman777/pdf-merger/badge/main)](https://www.codefactor.io/repository/github/alexroman777/pdf-merger/overview/main)
[![CodeQL](https://github.com/AlexRoman777/PDF-Merger/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/AlexRoman777/PDF-Merger/actions/workflows/github-code-scanning/codeql)

---

A simple program to merge multiple PDF files into one PDF file.

Recently I had to merge multiple PDF files. I found a few online websites/tools that could do this, but I wanted to do it locally on my computer. So here is a simple script that does just that.

It uses the [PyPDF](https://pypdf.readthedocs.io/en/stable/index.html#) library to merge the PDF files. The library can do a lot more than just merging PDF files, but for my use case, I just needed to merge PDF files.

---

## How it looks

Select the PDF files you want to merge.

<img src="img/select.png" alt="PDF Merger" width=45%/>

---

Resulting PDF file.

<img src="img/merged.png" alt="PDF Merger" width=45%/>

---

Terminal output.

<img src="img/terminal.png" alt="PDF Merger" width=45%/>

---

## Usage

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
python3 src/main.py
```

---
