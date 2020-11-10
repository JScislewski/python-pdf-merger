import PyPDF4, os

files = []

for file in os.listdir("."):
    if file.endswith(".pdf"):
        files.append(file)

files.sort(key=str.lower)
pdf_writer = PyPDF4.PdfFileWriter()

for file in files:
    file_obj = open(file, "rb")
    pdf_reader = PyPDF4.PdfFileReader(file_obj)

    for page in range(0, pdf_reader.getNumPages()):
        page_obj = pdf_reader.getPage(page)
        pdf_writer.addPage(page_obj)

output = open("merged.pdf", "wb")
pdf_writer.write(output)
output.close()
