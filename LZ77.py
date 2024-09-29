def lz77_encode(path_in, path_out, window_size=20):
    i = 0
    file = open(path_in, 'r', encoding = 'utf-8')
    file2 = open(path_out, 'w', encoding = 'utf-8')
    encoded_data = []
    s = file.read()
    while i < len(s):
        match = (0, 0, s[i])

        for j in range(max(0, i - window_size), i):
            length = 0
            while i + length < len(s) and s[j + length] == s[i + length]:
                length += 1

            if length > match[1]:
                match = (i - j, length, s[i + length] if i + length < len(s) else '')

        if match[1] > 0:
            encoded_data.append((match[0], match[1], match[2]))
            i += match[1] + 1
        else:
            encoded_data.append((0, 0, s[i]))
            i += 1

    return encoded_data


def lz77_decode(encoded_data, path_out):
    decoded_string = []
    file2 = open(path_out, 'w', encoding='utf-8')
    for shift, length, next_char in encoded_data:
        if shift > 0:
            start = len(decoded_string) - shift
            for i in range(length):
                decoded_string.append(decoded_string[start + i])

        if next_char:
            decoded_string.append(next_char)
    decoded_stringg = ''.join(decoded_string)
  #  print(decoded_stringg)
    file2.write(decoded_stringg)
    return ''.join(decoded_string)
