# The PhD thesis template
A (unofficial) LaTeX template for creating a PhD thesis at the Department of Mathematics, Stockholm University.

## The structure of a PhD thesis
A cumulative dissertation style thesis at the Department of Mathematics, Stockholm University, consists of the
following parts:
1. The cover page
2. The "spikblad" or "nailing page" containing publication information and the abstract
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
whereafter it can be included by uploading the `pdf` to the thesis publication tool.
Item 10 is handled by uploading the individual papers to the thesis publication tool.
The rest is handled by this LaTeX template.

## The structure of this template
The main file for items 4-9 is `main.tex`.
It is structured in order to make it graspable by utilizing the `input` command to include the various parts
of the thesis as well as loading the necessary packages and defining the necessary commands.
This guide will go through everything you need to use the template and compile everything into a series of `pdf` files
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
extra work (see Step 4 in the usage section below).

## Usage
This guide will go through the steps to use the template, from opening it up to 
compiling the final document and uploading it to the thesis publication tool.

### Step 1: Copy the template
The first step is to download the template and copy it to a new folder.
This can be done using a terminal command like this:
```bash
git clone https://github.com/henningzakrisson/su-math-thesis
copy -r su-math-thesis my_thesis
cd my_thesis
```
Or by downloading the repository as a zip file (Press the green "Code" button and select "Download ZIP"),
extracting it, and renaming the folder to something like `my_thesis`.
The `my_thesis` folder is where you will work on your thesis.

### Step 2: Compile the dummy document
In order to make sure everything works on your system, compile the dummy document.
I recommend using `pdflatex` for this, using `biber` for the bibliography.
I also recommend using a `interim` folder for the compilation, as this will generate a lot of files.
The `interim` folder is added in the `.gitignore` file, so it will not be included in the repository.
The same goes for the `out` folder, which will be touched upon later.

Compile using whatever software you prefer, but here is a suggestion for the terminal:
```bash
mkdir interim
pdflatex -output-directory=interim main.tex
biber interim/main
pdflatex -output-directory=interim main.tex
pdflatex -output-directory=interim main.tex
```
This will generate a `main.pdf` file in the `interim` folder.
Check that this looks good and that the references are correct.

For future compilations, use the same commands without the `mkdir` command.
Also, unless you change the references, you only need to run 
```bash
pdflatex -output-directory=interim main.tex
```
for a recompilation.

### Step 3: Write the thesis
This is probably the hardest part.
The `src` folder is where to put all the source code for the thesis.
I suggest using a folder structure that makes sense to you, and that you are consistent with it.
Add chapters, sections, and subsections to the thesis by using the `input` command in `main.tex`.
You can see in the dummy example how this is done.
If you add new sources, make sure to add them to the `bibliography.bib` file.

### Step 4: Preprocess the papers (optional)
If you want the page numbering to be consistent throughout the entire thesis, you can add the papers to the 
`src/papers` folder.
Performing this step  will also include the individual papers in the table of contents.
What this means is that if you just upload the papers to the thesis publication tool, the page numbering will
use whatever page numbering the `pdf` files have, typically that of the journal they were published in,
or the page numbering of the preprint.

If you do not care for this, you can remove the `papers` folder and the `input` command in `main.tex` that includes
a paper.
Do however _not_ remove the Part II section named Papers, since this should still separate the introduction from the
papers.

To remove the page numbering from the papers, open their source `tex` files and add the following command
at the beginning of the document:
```latex
\pagenumbering{gobble}
```

Then, add the compiled papers to the `src/papers` folder, and add it to the thesis using these two lines:
```latex
\part*{Paper I\addcontentsline{toc}{section}{Paper X}}
\includepdf[pages=-, pagecommand={\thispagestyle{plain}}]{src/papers/paper_x.pdf}
```
in `main.tex`, replacing `Paper X` with the roman numeral number of the paper and `paper_x.pdf` with the name of the `pdf` file.
An example for this is included in the dummy document.

#### Step 4.1 Removing pages from already compiled papers (optional)
In case you do not have access to the source files of the papers, the situation is a little more complicated
since you will have to remove the page numbers from the `pdf` files.
My suggestion is to create a new `LaTeX` document that includes the papers using the `pdfpages` package,
but uses `tikz` to create a white overlay on top of the page numbers.
It takes a bit of manual work, but it is doable.
I have not finished my general implementation of this to add to this template.
Note that this way you can also remove annoying headers and footers that are often included
in digitally published papers.

#### Step 4.2 Removing colored hyperlinks from the papers (optional)
When printing the thesis, the library will ask you to specify on what pages to print in color.
This is in order to make figures and plots look good.
However, many digital publications use colored hyperlinks.
Thus, if pages with figures are printed in colors, and pages without figures are printed in black and white,
the hyperlinks will only be visibly colored on some pages, looking inconsistent.

While this is extremely minor, there is a simple solution to this, which is to run the `ghostscript` included
in the `scripts` folder on the `pdf` files of the papers.
Run the command in the terminal like this:
```bash
./scripts/remove_hyperlinks.sh src/papers/output.pdf src/papers/input.pdf
```
where `output.pdf` is the name of the new file and `input.pdf` is the name of the original file.
Check that the result looks good, and if it does, use the new file in the thesis.

### Step 5: Compile the final document
When you are done writing the thesis, it is time to compile the final document
and split it into the various parts that can be uploaded to the thesis publication tool.
This can be done by compiling as normal and then manually splitting the resulting `pdf` file,
but an easier way is to use the `python` script included in the `scripts` folder, that
splits the `pdf` file into the various parts by examining the table of contents.
Note that this requires the `PyPDF2` package, which can be installed using `pip`:
```bash
pip install PyPDF2
```
If you have changed the format of the table of contents, or drastically changed the structure of the thesis,
the script likely won't work, and you will have to split the `pdf` manually.
It also won't work if you have more than 9 papers, but that is easily adjusted manually in the script.

To compile and split the final document, use the following commands (all included in the `scripts/compile_and_split.sh` shell script):
```bash
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
```
This will create a number of files in the `out` folder.
1. `abstract.pdf` - For publication purposes, this file can be discarded, as it will be replaced by the spikblad. It is however useful to include when sending the thesis to internal revision or
    to the opponent and grading committee.
2. `frontmatter.pdf` - This is the part of the frontmatter that is not included in the thesis publication tool.
    It contains the List of papers, Acknowledgements, and Table of contents.
3. `introduction.pdf` - This is the introduction, or the "kappa".
    It starts with the "Part I" title page and ends with the "Part II" title page.
4. `paper_i.pdf`, `paper_ii.pdf`, ... - These are the papers included in the thesis.
    If you did not perform Step 4, these files won't be included in the `out` folder.

### Step 6: Upload to the thesis publication tool
When you have the `pdf` files, you can upload them to the thesis publication tool.

The spikblad/nailing page/abstract will be provided by the _Avhandlingsstöd_ department after registering the thesis
and should be uploaded as a separate file under the "Spikblad"/"Nailing page" section in the tool

The `frontmatter.pdf` and `introduction.pdf` files should be uploaded under the "Kappa/Thesis" section in the
tool, in that order.

The papers `paper_i.pdf`, `paper_ii.pdf`, ... should be uploaded under the "Papers" section in the tool.
Make sure to upload them in the correct order.
If you did not perform Step 4, upload the original `pdf` files of the papers instead.

Check the preview in the tool and make sure that the numberings in the pages and table
of contents are correct.
If anything is wrong with these, the easiest solution is probably to go back to the source files and 
manually add the command
```latex
\setcounter{page}{X}
```
where `X` is the correct page number, and recompile the document.
Hopefully, this will not be necessary.

## Troubleshooting
Sometimes the page numbering will be off, especially in the frontmatter which should feature
unlabeled, roman, page numberings. To supress page numberings in the frontmatter when it pops up,
use the command
```latex
\thispagestyle{empty}
```
or
```latex
\afterpage{\null\thispagestyle{empty}
\newpage}
```
until you reach a satisfactory page numbering.
This will likely happen if some section in the frontmatter extends beyond one page.

If at any point in the thesis you end up with Chapter titles or new papers on the left-hand side,
you can use the command
```latex
\cleardoublepage
```
or
```latex
\newpage
```
until you reach a satisfactory page numbering.
Also, if the number is just plain wrong anywhere, use
```latex
\setcounter{page}{X}
```
where `X` is the correct page number.

## Not implemented
 - A solution to the fact the frontmatter pages are occasionally visibly numbered
and have to be supressed manually
 - Reimplementing the template as a `cls` file for easier use
 - A straight-forward way to remove page numbers from `pdf` files

## Contact
If you have any questions or suggestions, feel free to contact me [here](mailto:henning.zakrisson@gmail.com).
I do not guarantee that I will be able to help or have time to help, but hopefully this template will
get a life of its own and be improved on by future PhD students.

Good luck with your thesis!
