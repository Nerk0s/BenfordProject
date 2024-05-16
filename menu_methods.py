import os

import read_file


def all_folders(exel_files, pptx_files, docx_files, txt_files, pdf_files):
    pass


def single_folder(exel_files, pptx_files, docx_files, txt_files, pdf_files):
    pass


def single_file(exel_files, pptx_files, docx_files, txt_files, pdf_files):
    global file_name
    extension = ""
    print("Single file mode")
    print("Choose file type:")
    print("1. Excel")
    print("2. PowerPoint")
    print("3. Word")
    print("4. Text")
    print("5. PDF")
    print("6. Back")
    selection = False
    exel = False
    pptx = False
    docx = False
    txt = False
    pdf = False
    back = False

    while not selection:
        choice = input("Enter choice: ")
        if choice == "1":
            selection = True
            exel = True
            print("Excel")
        elif choice == "2":
            selection = True
            pptx = True
            print("PowerPoint")
        elif choice == "3":
            selection = True
            docx = True
            print("Word")
        elif choice == "4":
            selection = True
            txt = True
            print("Text")
        elif choice == "5":
            selection = True
            pdf = True
            print("PDF")
        elif choice == "6":
            back = True
            selection = True
            print("Back")
        else:
            print("Invalid choice")
            single_file()

    if not back:
        list_files = []

        if exel:
            print("Exel files:")
            list_files = exel_files
        elif pptx:
            print("PowerPoint files:")
            list_files = pptx_files
        elif docx:
            print("Word files:")
            list_files = docx_files
        elif txt:
            print("Text files:")
            list_files = txt_files
        elif pdf:
            print("PDF files:")
            list_files = pdf_files

        # for i in range(len(list_files)):
        # Read file
    else:
        return back

    # file selection
    print("Choose the file you want to read:")
    selection = False
    while not selection:
        for i in range(len(list_files)):
            print(f"{i + 1}. {list_files[i]}")
        choice = input("Enter choice: ")

        for i in range(len(list_files)):
            if choice == list_files[i]:
                selection = True
                file_name = os.getcwd() + "\\" + "input" + "\\" + list_files[i]
                break
            elif choice == "back":
                return back
            else:
                print("Invalid choice")

    output = read_file.reader(file_name)
    return output


def all_files(exel_files, pptx_files, docx_files, txt_files, pdf_files):
    print("All files mode")
    print("Choose file type:")
    print("1. Excel")
    print("2. PowerPoint")
    print("3. Word")
    print("4. Text")
    print("5. PDF")
    print("6.All")
    print("7. Back")
    choice = input("Enter choice: ")

    if choice == "1":
        exel = True
        print("Excel")
    elif choice == "2":
        pptx = True
        print("PowerPoint")
    elif choice == "3":
        docx = True
        print("Word")
    elif choice == "4":
        txt = True
        print("Text")
    elif choice == "5":
        pdf = True
        print("PDF")
    elif choice == "6":
        all_files = True
        print("All")
    elif choice == "7":
        print("Back")
    else:
        print("Invalid choice")


def menu(selection_digit, exel_files, pptx_files, docx_files, txt_files, pdf_files):
    output = []
    if int(selection_digit) == 1:
        output = single_file(exel_files, pptx_files, docx_files, txt_files, pdf_files)
    elif int(selection_digit) == 2:
        output = all_files(exel_files, pptx_files, docx_files, txt_files, pdf_files)
    elif int(selection_digit) == 3:
        output = single_folder(exel_files, pptx_files, docx_files, txt_files, pdf_files)
    elif int(selection_digit) == 4:
        output = all_folders(exel_files, pptx_files, docx_files, txt_files, pdf_files)
    elif int(selection_digit) == 5:
        print("Exit")
        return "Exit"
    else:
        print("Invalid choice")
        return
    return output
