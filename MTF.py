def mtf_enc(path_in, path_out):  # Move-to-front

    # name = "out_BWT.txt"
    file = open(path_in, "rb")
    file2 = open(path_out, "wb")

    data = file.read()
    dictionary = list(range(256))
    data2 = bytearray(b'')
    num = 0
    print(99)

    for i in data:
        num = dictionary.index(i)
        data2.append(num)
        dictionary.pop(num)
        dictionary.insert(0, i)
    print(88)
    file2.write(data2)
    file.close()
    file2.close()


def mtf_dec(path_in, path_out):  # decode Move-to-Front

    file = open(path_in, "rb")
    file2 = open(path_out, "wb")

    data = file.read()
    dictionary = list(range(256))
    data2 = bytearray(b'')

    for i in data:
        data2.append(dictionary[i])
        d = dictionary.pop(i)
        dictionary.insert(0, d)

    file2.write(data2)
    file.close()
    file2.close()
