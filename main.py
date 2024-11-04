from PyPDF2 import PdfReader, PdfWriter

pdfwriter = PdfWriter()
pdf = PdfReader("1.pdf")

# Use len(reader.pages) instead of pdf.numPages
#The for loop iterates over each page in the PDF.

for page_num in range(len(pdf.pages)):
    pdfwriter.add_page(pdf.pages[page_num])  # Note the change from addPage to add_page

passw = "1234"
pdfwriter.encrypt(passw)

with open('passwordprotected.pdf', 'wb') as f:
    pdfwriter.write(f)
