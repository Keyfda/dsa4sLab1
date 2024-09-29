from PIL import Image
import numpy as np
import math


def rle_txt_enc(file_path, output_path):
    with open(file_path, "r", encoding="utf-8") as file:
        with open(output_path, "w", encoding="utf-8") as file2:

            data = file.read()
            k = 1

            for i in range(len(data) - 1):
                if data[i] == data[i + 1]:
                    k += 1
                else:
                    if k != 1:
                        file2.write(str(k))
                    if data[i].isdigit():
                        file2.write('`')
                    file2.write(data[i])
                    k = 1

            if k != 1:
                file2.write(str(k))
            if data[-1].isdigit():
                file2.write('`')
            file2.write(data[-1])

        file.close()
        file2.close()


def rle_txt_dec(file_path, output_path):
    file = open(file_path, "r", encoding="utf-8")
    file2 = open(output_path, "w", encoding="utf-8")

    data = file.read()
    nums = ""

    for i in range(len(data) - 1):
        if data[i].isdigit() and (i == 0 or data[i - 1] != '`'):
            nums += data[i]
        elif nums and data[i] != '`':
            file2.write(data[i] * int(nums))
            nums = ""
        elif data[i] != '`':
            file2.write(data[i])

    if len(nums) != 0 and data[-1] != chr(96):
        for _ in range(int(nums)):
            file2.write(str(data[-1]))
    elif data[-1] != chr(96):
        file2.write(data[-1])

    file.close()
    file2.close()
