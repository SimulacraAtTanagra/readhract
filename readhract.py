# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:08:00 2020

@author: sayers
"""
import PyPDF2
import pandas as pd
l = []

pdf_file = open('Y:\\HR-PROCEDURES-GUIDE-FINAL.pdf','rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
for i in range(read_pdf.getNumPages()):
    page = read_pdf.getPage(i)
    page_content = page.extractText()
    l.append(page_content)
    
pdfdb = pd.DataFrame(l, columns=['text'])
print (pdfdb)


def showthis(texts,i,x):
   if str((texts.splitlines()[i:x])).find(":")>0:
        return(texts.splitlines()[i+1:x+1])
   else:
        return(texts.splitlines()[i:x])
    
pdfdb['category'] = pdfdb.text.apply(showthis,args=(2,3))
pdfdb['specific_title'] = pdfdb.text.apply(showthis,args=(3,4))
pdfdb['action_type'] = pdfdb.text.apply(showthis,args=(14,15))
pdfdb['action_reason'] = pdfdb.text.apply(showthis,args=(16,17))
pdfdb['CFSA_loc'] = pdfdb.text.apply(showthis,args=(18,19))
pdfdb['Policyy'] = pdfdb.text.apply(showthis,args=(20,-10))
pdfdb['purpose'] = pdfdb.text.apply(showthis,args=(4,5))