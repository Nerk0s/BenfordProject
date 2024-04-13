"""
This Programm reads a single or a group of pdf files
and writes all digits in a single file or array
"""
import os

path = os.path.abspath(os.getcwd())
path_file = path + "/input/"
files = []

# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dir_list = os.listdir(path_file)
    print(dir_list)
    files: list[str] = dir_list

    for file in files:
        print(file)

    number: str = " "
    alphabet = ["a", "b", "c", "d", "e", "f",
                "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z"]
    i = 0

    for i, file in enumerate(files):
        print(str(i + 1) + ". " + file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
