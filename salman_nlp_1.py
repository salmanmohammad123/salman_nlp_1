#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 14:28:00 2023

@author: dragon
"""
from pdf2image import convert_from_path
import cv2
import pytesseract
import os

pdf = '/Users/salma/OneDrive/Desktop/Operations Management.pdf'

pages = convert_from_path(pdf,0)
print('All {} converted to images'.format(pdf))
img_count = 1
filename = (pdf.replace('.pdf','')).split('/')
for page in pages:
    img_name = ("{}_img_"+str(img_count)+".jpg").format(filename[-1])
    page.save(img_name,'JPEG')
    img_count += 1
    print(img_name,"image saved")
    
    img = cv2.imread(img_name)
    img = cv2.resize(img, (1240,1755))
    
    with open(('{}_FULL_PDF_TEXT.txt').format(filename[-1]), 'a') as output:
        print("output file created")
        text = str((pytesseract.image_to_string(img_name)))
        text = text.strip()
        output.write(text + "\n\n\n\n")
        print('text extracted of ',img_name)
    output.close()
    os.remove(img_name)
#%%

