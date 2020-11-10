import PyPDF4, os

files = []
for file in os.listdir("."):
    if file.endswith(".pdf"):
        files.append(file)
files.sort(key=str.lower)
pdf_writer = PyPDF4.PdfFileWriter()
print(files)
for file in files:
    file_obj = open(file, "rb")
    pdf_reader = PyPDF4.PdfFileReader(file_obj)
    for page in pdf_reader.numPages:
        page_obj = pdf_reader.getPage(page)
        pdf_writer.add(page_obj)
