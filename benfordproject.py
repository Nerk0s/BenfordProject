import os
import PyPDF2
import pptx
from docx import Document
import sys
import openpyxl
import menu_methods

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
folders = []
contain_folders = False

print(os.listdir(input_path))


def contain():
    for file in read_files_dir:
        if os.path.isdir(input_path + "\\" + file):
            folders.append(file)
            print("Folder found: " + file)
            contain_folders = True
        else:
            filename, fileExtension = os.path.splitext(file)
            if fileExtension == ".xlsx":
                exel_files.append(file)
            elif fileExtension == ".pptx":
                pptx_files.append(file)
            elif fileExtension == ".docx":
                docx_files.append(file)
            elif fileExtension == ".txt":
                txt_files.append(file)
            elif fileExtension == ".pdf":
                pdf_files.append(file)
            else:
                print("File extension not supported: " + fileExtension)


runnig = True

while runnig:
    contain()

    if contain_folders:
        contain()

    print(f'exel files: {exel_files}')
    print(f'pptx files: {pptx_files}')
    print(f'docx files: {docx_files}')
    print(f'txt files: {txt_files}')
    print(f'pdf files: {pdf_files}')
    print("Finished")
    # with open(input_path, 'r', encoding='utf8', errors='ignore') as file:

    # Menu to choose reading mode
    print("Choose reading mode:")
    print("Single file: 1")
    print("All files: 2")
    print("Single folder: 3")
    print("All folders: 4")
    print("Exit: 5")
    mode = input("Enter choice:")

    if mode == "1":
        output = menu_methods.menu(mode, exel_files, pptx_files, docx_files, txt_files, pdf_files)
        if output == "Exit":
            runnig = False
        else:
            print(output)
