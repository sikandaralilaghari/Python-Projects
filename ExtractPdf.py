import PyPDF2

pdf = open("ML_Project_Proposal.pdf", "rb")

reader = PyPDF2.PdfReader(pdf)

page = reader.pages[0]
print(page.extract_text())