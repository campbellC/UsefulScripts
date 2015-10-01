from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
assert len(sys.argv[1:]) % 2 == 0
for i,k in zip(sys.argv[1::2],sys.argv[2::2]):

    input1 = PdfFileReader(open(i,"rb"))
    input2 = PdfFileReader(open(k,"rb"))
    output1 = PdfFileWriter()

    size = input1.getNumPages()
    flag = False
    if input2.getNumPages() != size:
        flag = True
    for num in xrange(size):
        output1.addPage(input1.getPage(num))
        if num == size-1 and flag:
            break
        output1.addPage(input2.getPage(num))

    outputStream = file(i[:-4] + "joined.pdf","wb")
    output1.write(outputStream)

