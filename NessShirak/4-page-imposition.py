from PyPDF2 import PdfFileReader, PdfFileWriter, pdf
import os.path

def inputSignatureNumber(text):
    sigNum = input(text)
    while sigNum%4!=0:
        print "The number of pages per signature has to be a multiple of 4"
        sigNum = input(text)
    return sigNum

def inputFileName(text):
    name = raw_input(text)
    while not os.path.isfile(name):
        print "No such file exists"
        name = raw_input(text)
    return name


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

def makeSimpleSignature(listPages,numSigPages):
    listDoublePages = []
    for i in range(numSigPages/2):
        if i%2 == 1:
            listDoublePages.append( sideBySidePage(listPages[i],listPages[numSigPages-i-1]) )
        else:
            listDoublePages.append( sideBySidePage(listPages[numSigPages-i-1],listPages[i]) )
    return listDoublePages



fileName = inputFileName("Enter file name: ")
numSigPages = inputSignatureNumber("Pages per signature: ")
pdfReader = PdfFileReader(file(fileName,"rb"))


totalPages = pdfReader.getNumPages()
if totalPages%4==0 and totalPages%numSigPages==0:
    pdfWriter = PdfFileWriter()

    for j in range(0,totalPages,numSigPages*2):
        #separate pages to make first signature
        listPages = []
        for i in range(numSigPages):
            listPages.append(pdfReader.getPage(j+i))
        #make first signature
        listDoublePages1 = makeSimpleSignature(listPages,numSigPages)

        #separate pages to make second signature
        listPages = []
        for i in range(numSigPages):
            if j+numSigPages+i < totalPages:
                listPages.append(pdfReader.getPage(j+numSigPages+i))
            else:
                listPages.append(pdf.PageObject.createBlankPage(pdfReader))
        #make second signature
        listDoublePages2 = makeSimpleSignature(listPages,numSigPages)

        listCuadruplePages = []
        if j+numSigPages*2 <= totalPages: #even number of signatures
            for i in range(numSigPages/2):
                listCuadruplePages.append( topToBottomPage(listDoublePages1[i],listDoublePages2[i]) )
        else: #odd number of signatures
            for i in range(numSigPages/4):
                listCuadruplePages.append( topToBottomPage(listDoublePages1[i],listDoublePages1[i+numSigPages/4]) )

        for page in listCuadruplePages:
            pdfWriter.addPage(page)

    f = open("imposed-"+fileName, "wb")
    pdfWriter.write(f)
    f.close()
elif totalPages%4!=0:
    print "The number of pages in your document should be a multiple of 4!"
else:
    print "The number of pages of your document and your signatures don't fit!"
