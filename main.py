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

    digit_array = []

    number: str = ""  #empty string to store the number
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z"]
    i = 0
    for i, file in range(len(files)):
        number: str = str(i + 1) + ". "
        print(number + files[i])

    for i, file in enumerate(files):
        with open(path_file + files[i], "r", encoding="utf-8") as f:
            for line in f:
                for char in line:
                    if char.isdigit():
                        print("Placeholder")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
