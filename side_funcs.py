def custom_sort_key(s):
    return [ord(c) if c != '.' and  c != '$' else 123 for c in s]


def suffix_array_naive(s):
    suffixes = [(s[i:], i) for i in range(len(s))]
    print(suffixes)
    sorted_suffixes = sorted(suffixes, key=lambda x: custom_sort_key(x[0]))
    print(sorted_suffixes)
    return [suffix[1] for suffix in sorted_suffixes]


def bwt_from_suffix_array(s, suffix_array):
    bwt = []

    for i in suffix_array:
        if i == 0:
            bwt.append(s[-1])
        else:
            bwt.append(s[i-1])
    print(bwt)
    return ''.join(bwt)


def classify_suffixes(s):
    n = len(s)
    suffix_types = [''] * n
    suffix_types[-1] = 'S'

    for i in range(n - 2, -1, -1):
        if s[i] > s[i + 1]:
            suffix_types[i] = 'L'
        elif s[i] < s[i + 1]:
            suffix_types[i] = 'S'
        else:
            suffix_types[i] = suffix_types[i + 1]

    return ''.join(suffix_types)


def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        s = file.read().strip()

    suffix_array = suffix_array_naive(s)

    bwt = bwt_from_suffix_array(s, suffix_array)

    suffix_types = classify_suffixes(s)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Суффиксный массив: " + str(suffix_array) + "\n")
        file.write("Последний столбец BWT: " + bwt + "\n")
        file.write("Типы суффиксов: " + suffix_types + "\n")



