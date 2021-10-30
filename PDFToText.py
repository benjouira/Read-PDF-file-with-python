from PyPDF2 import PdfFileReader,PdfFileWriter

# put here your pdf file name
pdf = PdfFileReader('yourFile.pdf')

# chose a name you want for your txt file 
with open('newFileName.txt','w') as f:
  
  for pageNumber in range (pdf.numPages):
    print('Page: {0}'.format(pageNumber))
    pageObj = pdf.getPage(pageNumber)
    try :
      txt=pageObj.extractText()
      print(''.center(100,'-'))
    except :
      pass
    else:
      f.write('Page {0}\n'.format(pageNumber+1))
      f.write(''.center(100,'-'))
      f.write(txt)
  f.close()


import pandas as pd
df=pd.read_csv("newFileName.txt", sep = "\t")
