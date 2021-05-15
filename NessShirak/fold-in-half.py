from PyPDF2 import PdfFileReader, PdfFileWriter, pdf
import os.path

def inputFileName(text):
    name = raw_input(text)
    while not os.path.isfile(name):
        print "No such file exists"
        name = raw_input(text)
    return name

def yesNoInput(text):
    choice = raw_input(text + " (y/n): ")
    while choice != "y" and choice != "Y" and choice != "n" and choice != "N":
        print "Please choose y or n"
        choice = raw_input(text + " (y/n): ")
    if choice == "y" or choice == "Y":
        return True
    return False


def topToBottomPage(page1, page2):
    ancho = page1.mediaBox.upperRight[0]
    alto = page1.mediaBox.upperRight[1]*2

    page = pdf.PageObject.createBlankPage(None,ancho,alto)
    page.mergePage(page2)
    page.mergeTranslatedPage(page1,0,alto/2)

    return page


def sideBySidePage(page1, page2):
    ancho = page1.mediaBox.upperRight[0]*2
    alto = page1.mediaBox.upperRight[1]
    
    page = pdf.PageObject.createBlankPage(None,ancho,alto)
    page.mergePage(page1)
    page.mergeTranslatedPage(page2,ancho/2,0)

    return page

fileName = inputFileName("Enter file name: ")
pdfReader = PdfFileReader(file(fileName,"rb"))


totalPages = pdfReader.getNumPages()
pageList = []
for i in range(totalPages):
    pageList.append(pdfReader.getPage(i))

choice = yesNoInput("Fold?")
while choice:
    newPageList = []
    ancho = pageList[0].mediaBox.upperRight[0]
    alto = pageList[0].mediaBox.upperRight[1]
    #ancho < alto -> put pages side by side
    if ancho < alto:
        for i in range(0, totalPages, 4):
            #making first page
            if i+2 < totalPages:
                newPageList.append(sideBySidePage(pageList[i],pageList[i+2]))
            else:
                newPageList.append(sideBySidePage(pageList[i],pdf.PageObject.createBlankPage(None,ancho,alto)))
            #making second page
            if i+1 < totalPages:
                if i+3 < totalPages:
                    newPageList.append(sideBySidePage(pageList[i+3],pageList[i+1]))
                else:
                    newPageList.append(sideBySidePage(pdf.PageObject.createBlankPage(None,ancho,alto),pageList[i+1]))
            else:
                newPageList.append(sideBySidePage(pdf.PageObject.createBlankPage(None,ancho,alto),pdf.PageObject.createBlankPage(None,ancho,alto)))
    else: #alto <= ancho -> put pages top to bottom
        for i in range(0, totalPages, 4):
            #making first page
            if i+2 < totalPages:
                newPageList.append(topToBottomPage(pageList[i],pageList[i+2]))
            else:
                newPageList.append(topToBottomPage(pageList[i],pdf.PageObject.createBlankPage(None,ancho,alto)))
            #making second page
            if i+1 < totalPages:
                if i+3 < totalPages:
                    newPageList.append(topToBottomPage(pageList[i+1],pageList[i+3]))
                else:
                    newPageList.append(topToBottomPage(pageList[i+1],pdf.PageObject.createBlankPage(None,ancho,alto)))
            else:
                newPageList.append(topToBottomPage(pdf.PageObject.createBlankPage(None,ancho,alto),pdf.PageObject.createBlankPage(None,ancho,alto)))
    del pageList[:]
    totalPages = len(newPageList)
    for i in range(totalPages):
        pageList.append(newPageList[i])
    
    choice = yesNoInput("Keep folding?")

pdfWriter = PdfFileWriter()
for page in pageList:
    pdfWriter.addPage(page)

f = open("folded-"+fileName, "wb")
pdfWriter.write(f)
f.close()
