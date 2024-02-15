import re
import argparse
import logging
import os

import PyPDF2


def count_papers(toc_content):
    # Regex pattern to match lines with "Paper I" to "Paper IX"
    pattern = (
        r"\\contentsline \{section\}\{\\numberline \{\d+\.\d+\}Paper [I,V,X]{1,3}\}"
    )
    matches = re.findall(pattern, toc_content)
    return len(matches)


def convert_to_roman(num, uppercase=True):
    val = [50, 40, 10, 9, 5, 4, 1]
    syb = ["L", "XL", "X", "IX", "V", "IV", "I"]

    if not uppercase:
        syb = [s.lower() for s in syb]

    roman_num = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1

    return roman_num


def extract_page_labels(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        if not reader.trailer["/Root"].get("/PageLabels"):
            # If no custom labels, default to sequential numbering
            return [str(i + 1) for i in range(len(reader.pages))]

        number_tree = reader.trailer["/Root"]["/PageLabels"]["/Nums"]
        labels = []

        for index in range(0, len(number_tree) - 1, 2):
            base_page = number_tree[index]
            label_info = number_tree[index + 1]
            label_style = label_info["/S"].upper() if "/S" in label_info else None
            next_base_page = (
                number_tree[index + 2]
                if index + 2 < len(number_tree)
                else len(reader.pages)
            )

            start = label_info.get("/St", 1)
            count = next_base_page - base_page

            if label_style == "/D":
                labels.extend([start + i for i in range(count)])
            elif label_style == "/R":
                for i in range(count):
                    labels.append(
                        convert_to_roman(
                            start + i, uppercase=(label_info["/S"] == "/R")
                        )
                    )
            else:
                labels.extend([str(base_page + i) for i in range(count)])

        return labels


def int_to_roman(num):
    roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return roman_numerals[num - 1]


def extract_page(title, toc_content):
    # This pattern captures the page number of the desired titles
    pattern = re.compile(
        r"\\contentsline \{.*?\}\{(?:I\\hspace \{1em\})?"
        + re.escape(title)
        + r"\}\{(.*?)\}",
        re.DOTALL,
    )
    match = pattern.search(toc_content)
    if match:
        return match.group(1)
    return None


def main():
    # Get file paths from command line arguments
    parser = argparse.ArgumentParser(description="Split document.")
    parser.add_argument("--toc_path", required=True, help="Path to the TOC file")
    parser.add_argument("--pdf_path", required=True, help="Path to the PDF file")
    parser.add_argument(
        "--out_path", required=True, help="Path to the output directory"
    )
    args = parser.parse_args()
    toc_path = args.toc_path
    pdf_path = args.pdf_path
    out_path = args.out_path

    log_file = os.path.join(out_path, "pdf_split.log")

    # Configure the logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # File handler
    fh = logging.FileHandler(log_file, mode="w")  # add mode='w'
    fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(fh)

    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
    logger.addHandler(ch)

    logging.info("Fetching Table of Contents")
    with open(toc_path, "r") as f:
        toc_content = f.read()

    n_papers = count_papers(toc_content)

    # List of titles that extract page numbers should be extracted for
    sections = ["abstract", "frontmatter", "introduction"]
    for i in range(1, n_papers + 1):
        sections.append(f"paper_{i}")

    titles = {
        "abstract": "Abstract",
        "frontmatter": "List of papers",
        "introduction": "Introduction",
    }
    for i in range(1, n_papers + 1):
        titles[f"paper_{i}"] = f"Paper {int_to_roman(i)}"

    # Extract page numbers
    start_pages = {}
    for section in sections:
        title = titles[section]
        page_number = extract_page(title, toc_content)
        if page_number:
            # If it is a integer, convert it to an int
            try:
                page_number = int(page_number)
            except ValueError:
                pass

            # if it is a paper, add two pages to skip the title page
            if section.startswith("paper"):
                page_number += 2
            start_pages[section] = page_number

    # Get all pages from pdf
    page_labels = extract_page_labels(pdf_path)

    # Create a dict that maps page labels to page numbers by their position in the list
    page_actual = {page_label: i + 1 for i, page_label in enumerate(page_labels)}

    # Get end pages
    end_pages = {}
    # Abstract is one page
    end_pages = {"abstract": start_pages["abstract"]}
    # Frontmatter is up until the last roman numeral in page_labels
    for i, label in enumerate(page_labels):
        if isinstance(label, int):
            end_pages["frontmatter"] = page_labels[i - 1]
            break

    # The rest of the sections are up until the next one minus three
    # (two for the title page and one for the blank page)
    for section in sections[2:-1]:
        try:
            end_pages[section] = start_pages[sections[sections.index(section) + 1]] - 3
        except ValueError:
            pass

    # Last paper is up until the end
    end_pages[sections[-1]] = page_labels[-1]

    # For each paper, split the pdf
    logging.info("Splitting PDF")
    for section in sections:
        start_page = page_actual[start_pages[section]]
        end_page = page_actual[end_pages[section]]
        pdf = PyPDF2.PdfReader(pdf_path)
        pdf_writer = PyPDF2.PdfWriter()
        for page in range(start_page, end_page + 1):
            pdf_page = pdf.pages[page - 1]
            pdf_writer.add_page(pdf_page)
        with open(f"{out_path}{section}.pdf", "wb") as f:
            pdf_writer.write(f)
            logging.info(f"Created {section}.pdf")


if __name__ == "__main__":
    main()
