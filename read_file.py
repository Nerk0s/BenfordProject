import math
import os
import PyPDF2
import pptx
from docx import Document
import sys
import openpyxl


def reader(file):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    with (open(file, 'r', encoding='utf8', errors='ignore') as file):
        content = file.read()
        content = content.replace('\n', '')
        for letter in alphabet:
            count = content.replace(letter, '')

        # benford's law
        # 30.1% of the time the first digit is 1
        # 17.6% of the time the first digit is 2
        # 12.5% of the time the first digit is 3
        # 9.7% of the time the first digit is 4
        # 7.9% of the time the first digit is 5
        # 6.7% of the time the first digit is 6
        # 5.8% of the time the first digit is 7
        # 5.1% of the time the first digit is 8
        # 4.6% of the time the first digit is 9
        # 0.0% of the time the first digit is 0

        # count the number of times each digit appears
        probab = []
        container1 = 0
        container2 = 0
        container1_2 = 0
        container2_2 = 0
        for i in range(1, 10):
            container1 = math.log10((1 + i) / i)
            container2 = math.log10((1 + i) / i)
# looks if the frequency of the digit is the same as the benford's law
            # TODO: check if the frequency of the digit is the same as the benford's law


            if container1 == container2:
                probab.append(container1)

        return probab
