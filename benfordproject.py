import os
import PyPDF2
import pptx
from docx import Document
import sys
import openpyxl

print("Starting")
input_path = os.getcwd() + "\\" + "input"
read_files_dir = os.listdir(input_path)
exel_files = []
pptx_files = []
docx_files = []
txt_files = []
pdf_files = []
filename = ""
fileExtension = ""

for file in read_files_dir:
    if file.endswith('.xlsx'):
        exel_files.append(file)
    elif file.endswith('.pptx'):
        pptx_files.append(file)
    elif file.endswith('.docx'):
        docx_files.append(file)
    elif file.endswith('.txt'):
        txt_files.append(file)
    elif file.endswith('.pdf'):
        pdf_files.append(file)
    else:
        print(f'Unsupported file format for file: {file}')

print(txt_files)
print(pdf_files)
# with open(input_path, 'r', encoding='utf8', errors='ignore') as file:
