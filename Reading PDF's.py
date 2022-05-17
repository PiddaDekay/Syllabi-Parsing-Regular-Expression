# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 11:30:02 2020

@author: dnehoran
"""

# importing required modules 
import PyPDF2 

# creating a pdf file object 
pdfFileObj = open('ARTS 007 (Canvas).pdf', 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# printing number of pages in pdf file 
print(pdfReader.numPages) 

# creating a page object 
pageObj = pdfReader.getPage(0) 

# extracting text from page 
print(pageObj.extractText()) 

# closing the pdf file object 
pdfFileObj.close() 
