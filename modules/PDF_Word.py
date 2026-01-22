from pdf2docx import Converter

    # PDF file path
pdf_file = "FInal.pdf"      # PDF file path
word_file = "output.docx"   # Word file path

cv = Converter(pdf_file)
cv.convert(word_file)
cv.close()

print("PDF successfully converted to Word!")
