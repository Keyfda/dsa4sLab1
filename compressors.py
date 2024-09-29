def bwt_naive_enc(p):
    in_str = p
    file = open('tests/texts/bwt_naive_log.txt', "w", encoding="utf-8")
    n = len(in_str)
    rotations = [in_str[-i:] + in_str[:-i] for i in range(n)]

    if len(in_str) < 20:
        rotations_str = '\n'.join(rotations)
        file.write('Permutations:\n')
        file.write(rotations_str)

    rotations = sorted(rotations, key=custom_sort_key)

    if len(in_str) < 20:
        rotations_str = '\n'.join(rotations)
        file.write('\n\nSorted:\n')
        file.write(rotations_str)

    encoded_data = [rotation[-1] for rotation in rotations]
    index = rotations.index(in_str)

    file.close()
    return index, encoded_data


def bwt_naive_dec(encoded_data, index):
    n = len(encoded_data)
    table = [''] * n

    for _ in range(n):
        table = sorted([encoded_data[i] + table[i] for i in range(n)], key=custom_sort_key)
    return table[index]


def custom_sort_key(s):
    return [ord(c) if c != '.' else 123 for c in s]


def bwt_enc(data):
    N = 5
    L = len(data)
    indices = []
    data2 = []

    for i in range(0, L, N):
        chunk = data[i:i + N]

        if not chunk:
            break

        index, transformed_chunk = bwt_naive_enc(chunk)
        indices.append(index)
        data2.extend(transformed_chunk)

    return data2, indices


def bwt_dec(data, indices):
    N = 5
    L = len(data)
    data2 = []

    for i in range(0, L, N):
        chunk = data[i:i + N]
        if not chunk:
            break
        index = indices[i // N]
        transformed_chunk = bwt_naive_dec(chunk, index)
        data2.extend(transformed_chunk)

    return data2


def rle_txt_enc(data):
    data2 = []
    k = 1

    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            k += 1
        else:
            if k != 1:
                data2.append(str(k))
            if data[i].isdigit():
                data2.append('`')
            data2.append(data[i])
            k = 1

    if k != 1:
        data2.append(str(k))
    if data[-1].isdigit():
        data2.append('`')
    data2.append(data[-1])

    return data2


def rle_txt_dec(data):
    decoded_data = []
    nums = ""

    for i in range(len(data)):
        if data[i].isdigit() and (i == 0 or data[i - 1] != '`'):
            nums += data[i]
        elif nums and data[i] != '`':
            count = int(nums)
            for _ in range(count):
                decoded_data.append(data[i])
            nums = ""
        elif data[i] != '`':
            decoded_data.append(data[i])

    if nums:
        if data[-1] != '`':
            count = int(nums)
            for _ in range(count):
                decoded_data.append(data[-1])
    elif data[-1] != '`':
        decoded_data.append(data[-1])

    return decoded_data



def mtf_enc(text):
    alphabet = list(range(256))
    encoded_output = []

    for byte_value in text:
        index = alphabet.index(byte_value)
        encoded_output.append(index)
        alphabet.pop(index)
        alphabet.insert(0, byte_value)

    return encoded_output


def mtf_dec(encoded_output):
    alphabet = list(range(256))
    decoded_output = []

    for index in encoded_output:
        byte_value = alphabet[index]
        decoded_output.append(byte_value)
        alphabet.pop(index)
        alphabet.insert(0, byte_value)

    return decoded_output
