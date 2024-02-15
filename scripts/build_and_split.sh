#!/bin/bash

# Navigate to the root directory
cd "$(dirname "$0")/.."

# Ensure interim and out directories exist
mkdir -p interim out

# Compile the document
pdflatex -interaction=batchmode --output-directory=interim main.tex
biber interim/main.aux
pdflatex -interaction=batchmode --output-directory=interim main.tex
pdflatex -interaction=batchmode --output-directory=interim main.tex

# Split it into pieces
python3 scripts/split_document.py --toc_path interim/main.toc --pdf_path interim/main.pdf --out_path out/
