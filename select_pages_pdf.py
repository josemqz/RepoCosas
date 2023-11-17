from PyPDF2 import PdfReader, PdfWriter

pdf_path = '.\Avance_Quezada_Jose_3.pdf'
file_base_name = pdf_path.replace('.pdf', '')

pdf = PdfReader(pdf_path)

pgs = list(range(9,28))
pdfWriter = PdfWriter()

for p in pgs:
    pdfWriter.add_page(pdf.pages[p])

with open('(0)_subset.pdf', 'wb') as f:
    pdfWriter.write(f)
    f.close()