import PyPDF4, os

pdf_files = []
for filename in os.listdir("."):
    if filename.endswith(".pdf"):
        pdf_files.append(filename)
pdf_files.sort(key=str.lower)
pdf_writer = PyPDF4.PdfFileWriter()
print(pdf_files)
