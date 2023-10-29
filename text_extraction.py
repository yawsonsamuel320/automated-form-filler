# Import libraries
from PyPDF2 import PdfReader

# Import internal project file/functions
from extract_ner import extract_info

# Open PDF File
pdf_file = PdfReader(open("./data/sample.pdf", "rb"))

# Read all pages in the PDF
pages = [pdf_file.pages[i] for i in range(len(pdf_file.pages))]

# Join all the pages into a string
text_from_pdf = "\n".join([page.extract_text() for page in pages])

extract_info(text_from_pdf)