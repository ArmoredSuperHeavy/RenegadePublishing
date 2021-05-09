from PyPDF2 import PdfFileReader, PdfFileWriter, pdf

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



fileName = raw_input("Enter file name: ")
numSigPages = input("Pages per signature: ")
pdfReader = PdfFileReader(file(fileName,"rb"))

totalPages = pdfReader.getNumPages()
pdfWriter = PdfFileWriter()

for j in range(0,totalPages,numSigPages):
    #separate pages to make signature
    listPages = []
    for i in range(numSigPages):
        listPages.append(pdfReader.getPage(j+i))

    #make signature
    listDoublePages = makeSimpleSignature(listPages,numSigPages)

    for page in listDoublePages:
        pdfWriter.addPage(page)
    
f = open("imposed-"+fileName, "wb")
pdfWriter.write(f)
f.close()
