import pyttsx3                                  # For Speaking
import PyPDF2                                   # For PDF Reader

book = open('adatb.pdf', 'rb')                  # addatb.pdf Is PDF File Name
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()
for num in range(29, pages):                    # Starting From Page Number 29 To Last Page
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
