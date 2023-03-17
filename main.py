import pyttsx3
import PyPDF2

book = open('Eat_that_frog.pdf', 'rb')
reader = PyPDF2.PdfReader(book)
pages = len(reader.pages)
print(pages)

ebook = pyttsx3.init()
for num in range(10, 20):
    page = reader.pages[num]
    text = page.extract_text()
    ebook.say(text)
    ebook.runAndWait()
