# The PhD thesis template
A (unofficial) LaTeX template for creating a PhD thesis at the Department of Mathematics, Stockholm University.

## The structure of a PhD thesis
A cumulative dissertation style thesis at the Department of Mathematics, Stockholm University, consists of the
following parts:
1. The cover page
2. The "spikblad" containing publication information and the abstract
3. A series of frontmatter pages including the title, the dirt title, a dedication page and an optional quote
4. The list of papers
5. Acknowledgements
6. Table of contents
7. Part I: Introduction (the "kappa")
8. A summary in Swedish
9. A bibliography for the introduction
10. Part II: The papers (including the papers themselves)
11. A back cover page with a summary and author biography

Items 1, 3, and 11 are handled in the thesis publication tool _Verktyg för visuell identitet_.
Item 2 will be provided by the _Avhandlingsstöd_ department after registering the thesis,
whereafter it can be included by uploading the pdf to the thesis publication tool.
Item 10 is handled by uploading the separate papers to the thesis publication tool.
The rest is handled by this LaTeX template.

## The structure of this template
The main file for items 4-9 is `main.tex`.
It is structured in order to make it graspable by utilizing the `input` command to include the various parts
of the thesis as well as loading the necessary packages and defining the necessary commands.
This guide will go through everything you need to use the template and compile everything into a series of pdfs
that can be uploaded to the thesis publication tool.

Note that the template now contains a set of dummy papers, sections, figures, and commands in order to make
it easier to grasp. 
The texts and images are AI-generated nonsense and should be replaced with your own content.

### `bibliography.bib`
This is where to put the references for the introduction and the papers.
This guide will assume that you are using `bibtex` with the `biber` as your bibliography backend.
If you prefer some other setup, make sure to change the citation commands in the source
files, e.g. in `src/sections/list_of_papers.tex` which utilizes the custom `fullciteall` command.
There are comment lines detailing where to put your own papers, book sources and article sources.
These are merely guidelines and can be changed to fit your needs - the document will compile as 
long as the references are in the file and the citation commands are correct.

### `src`
This folder is meant to contain the source code for the entire thesis.
It is split into a number of folders.

#### `src/packages.tex`
This is where all `LaTeX` packages are loaded.
The current setup is quite minimal, but it is easy to add more packages here.
If you remove any package from here, make sure this does not cause issues elsewhere in the document.
I recommend adding all relevant packages here, as it makes it easier to keep track of what is loaded.

#### `src/setup_layout.tex`
This is where the layout of the document is set up.
This is done by using commands from some of the packages
loaded in `src/packages`.
A lot of this is customizable, but the current setup aligns with what
most previous theses have looked like.

#### `src/custom_commands.tex`
This contains a few custom commands used in the thesis.

For example, it sets up the official Stockholm University color scheme,
using the definitions from _Digital färgpalett_.
These can be used in figures for a nice and consistent look, but it is not mandatory.
For their names, see the file.
Some other commands included are for solving some issues with page numbering.
These are pretty hacky and work for the current setup, but might need to be changed
for future use.
The `fullciteall` command defined here is used in the list of papers to print all references in the bibliography.
This is also where you could add your own custom commands, like Definitions, Proofs, etc.
Currently, the "Remark" environment is defined here as an example.

#### `src/sections`
This is where to put the source code for the various sections of the thesis.
These can preferably be split into chapter- or section-wise folders, but it is up to the
author to decide how to structure this.
Some files included in this folder are:
 - `list_of_papers.tex` - The list of papers.
    This should outline the papers included in the thesis, and assign them roman numerals.
    A template for this is included, using the custom `fullciteall` command.
    The contribution of the thesis author should be outlined for all co-authored papers.
 - `acknowledgements.tex` - The acknowledgements for the thesis.
 - `sammanfattning.tex` - The summary in Swedish.
    Most theses use a translation of the abstract.

#### `src/algorithms`, `src/figures`, `src/tables`
These are only suggested directories for the source code for algorithms, figures, and tables.
Change it up if you prefer a different structure.

#### `src/papers`
This is where one can put the `pdf` files for the papers included in the thesis.
This is not mandatory and will only matter if you want the page numbering of the thesis
to be consistent throughout the entire thesis, which will require a bit of
extra work (see Step X in the usage section below).

## Usage

## Not implemented
 - A solution to the fact the frontmatter pages are occasionally visibly numbered
and have to be supressed manually
