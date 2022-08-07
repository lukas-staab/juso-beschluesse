# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import PyPDF2

def ocr_stuff():
    folder = "buko/"
    file = "Beschlussbuch-2021.pdf"
    with open("./ressources/" + folder + file, "rb") as f:
        reader = PyPDF2.PdfFileReader(f)
        text = ""
        for i in range(1, reader.numPages):
            page = reader.getPage(i)
            text = text + page.extractText()
            text = text + "-------------------\n"
        os.makedirs('./output/' + folder, exist_ok=True)
        with open('./output/' + folder + file + ".txt", 'w') as o:
            o.write(text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ocr_stuff()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
