import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# Ask the user to select a PDF file
book = askopenfilename(filetypes=[("PDF files", "*.pdf")])

if book:
    pdfreader = PyPDF2.PdfReader(book)
    pages = len(pdfreader.pages)
    player = pyttsx3.init()

    for num in range(pages):
        page = pdfreader.pages[num]
        text = page.extract_text()
        player.say(text)
        player.runAndWait()
else:
    print("No file selected.")