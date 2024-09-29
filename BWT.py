
import os

def bwt_naive_enc(p):
    #in_str = ".abrakadabra$"
    in_str = p
    # sArray = SufArray(in_str)
    # suffix_array = sArray.get_array()
    file = open('tests/texts/bwt_naive_log.txt', "w", encoding="utf-8")

    n = len(in_str)

    rotations = [in_str[-i:] + in_str[:-i] for i in range(n)]

    if len(in_str) < 20:
        rotations_str = '\n'.join(rotations)
        file.write('Permutations:\n')
        file.write(rotations_str)

    rotations = sorted(rotations, key=custom_sort_key)
    #print(rotations)

    if len(in_str) < 20:
        rotations_str = '\n'.join(rotations)
        file.write('\n\nSorted:\n')
        file.write(rotations_str)

    encoded_data = ''.join(rotation[-1] for rotation in rotations)
    index = rotations.index(in_str)

    file.close()
   # print(index)

    return index, encoded_data


def bwt_naive_dec(encoded_data, index):
    n = len(encoded_data)
    table = [''] * n

    for _ in range(n):
        table = sorted([encoded_data[i] + table[i] for i in range(n)], key=custom_sort_key)
       # print(table)
    a = table[index]
    #print(a)
    #print(table[index])
    return table[index]


def custom_sort_key(s):
    return [ord(c) if c != '.' else 123 for c in s]


def bwt_enc(path_in, path_out):
    N = 5
    write_f = open(path_out, 'w', encoding='utf-8')
    read_f = open(path_in, 'r', encoding='utf-8')

    L = os.path.getsize('tests/texts/RuText.txt')
    indices = []

    for i in range(0, L, N):
        in_str = read_f.read(N)
        if not in_str:
            break

        index, data2 = bwt_naive_enc(in_str)
        indices.append(index)
        data23 = ''.join(data2)
        write_f.write(data23)

    write_f.close()
    read_f.close()
    return in_str, indices


def bwt_dec(path_in, indices, path_out):
    write_f = open(path_out, 'w', encoding='utf-8', newline='\x0A')
    read_f = open(path_in, 'r', encoding='utf-8')


    N = 5

    L = os.path.getsize(path_in)

    for i in range(len(indices)):
        in_str = read_f.read(N)
        if not in_str:
            break

        index = indices[i]
        data2 = bwt_naive_dec(in_str, index)
        data23 = ''.join(data2)
        write_f.write(data23)

    write_f.close()
    read_f.close()
    return


def average_repeating_length():
    read_f = open('tests/texts/bwt_RuText_enc.txt', 'r', encoding='utf-8')
    s = read_f.read()
    total_length = 0
    count_sequences = 0
    total_repeats = 0

    i = 0
    while i < len(s):
        current_char = s[i]
        count = 1

        while i + 1 < len(s) and s[i + 1] == current_char:
            count += 1
            i += 1

        if count > 1:
            total_length += count
            count_sequences += 1
            total_repeats += count

        i += 1

    avg = total_repeats / count_sequences
    print(total_repeats)
    print(count_sequences)
    print(avg)
    if len(s) == 0:
        return 0

    average_length = (total_repeats - 2 * count_sequences) / len(s)
    print(average_length)
    return average_length


def average_repeating_length1():
    read_f = open('tests/texts/bwt_enwik7_enc.txt', 'r', encoding='utf-8')
    s = read_f.read()
    total_length = 0
    count_sequences = 0
    total_repeats = 0

    i = 0
    while i < len(s):
        current_char = s[i]
        count = 1

        while i + 1 < len(s) and s[i + 1] == current_char:
            count += 1
            i += 1

        if count > 1:
            total_length += count
            count_sequences += 1
            total_repeats += count

        i += 1

    avg = total_repeats / count_sequences
    print(total_repeats)
    print(count_sequences)
    print(avg)
    if len(s) == 0:
        return 0

    average_length = (total_repeats - 2 * count_sequences) / len(s)
    print(average_length)
    return average_length

def average_repeating_length2():
    read_f = open('tests/texts/RuText.txt', 'r', encoding='utf-8')
    s = read_f.read()
    total_length = 0
    count_sequences = 0
    total_repeats = 0

    i = 0
    while i < len(s):
        current_char = s[i]
        count = 1

        while i + 1 < len(s) and s[i + 1] == current_char:
            count += 1
            i += 1

        if count > 1:
            total_length += count
            count_sequences += 1
            total_repeats += count

        i += 1

    avg = total_repeats / count_sequences
    print(total_repeats)
    print(count_sequences)
    print(avg)
    if len(s) == 0:
        return 0

    average_length = (total_repeats - 2 * count_sequences) / len(s)
    print(average_length)
    return average_length


def average_repeating_length3():
    read_f = open('tests/texts/enwik7', 'r', encoding='utf-8')
    s = read_f.read()
    total_length = 0
    count_sequences = 0
    total_repeats = 0

    i = 0
    while i < len(s):
        current_char = s[i]
        count = 1

        while i + 1 < len(s) and s[i + 1] == current_char:
            count += 1
            i += 1

        if count > 1:
            total_length += count
            count_sequences += 1
            total_repeats += count

        i += 1

    avg = total_repeats / count_sequences
    print(total_repeats)
    print(count_sequences)
    print(avg)
    if len(s) == 0:
        return 0

    average_length = (total_repeats - 2 * count_sequences) / len(s)
    print(average_length)
    return average_length
