from collections import Counter
import heapq


class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freq_table):
    heap = [Node(symbol, freq) for symbol, freq in freq_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def build_huffman_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.symbol is not None:
            codebook[node.symbol] = prefix
        build_huffman_codes(node.left, prefix + "0", codebook)
        build_huffman_codes(node.right, prefix + "1", codebook)
    return codebook


def is_prefix_free(codes):
    sorted_codes = sorted(codes, key=len)
    for i in range(len(sorted_codes)):
        for j in range(i + 1, len(sorted_codes)):
            if sorted_codes[j].startswith(sorted_codes[i]):
                return False
    return True


def huffman_encode(path_in, path_out, group_size=5):
    with open(path_in, 'r', encoding='utf-8') as file:
        data = file.read()

    grouped_data = [
        data[i:i + group_size].replace(' ', '<SPACE>').replace('\n', '<NEWLINE>')
        for i in range(0, len(data), group_size)
    ]

    freq_table = Counter(grouped_data)
    root = build_huffman_tree(freq_table)
    huffman_codes = build_huffman_codes(root)

    if not is_prefix_free(huffman_codes.values()):
        print("Коды не являются префиксными!")
        return None

    encoded_data = ''.join([huffman_codes[symbol] for symbol in grouped_data])

    with open(path_out, 'w', encoding='utf-8') as codes_file:
        for symbol, code in huffman_codes.items():
            codes_file.write(f"{symbol}: {code}\n")

    with open(path_out, 'w', encoding='utf-8') as encoded_file:
        encoded_file.write(encoded_data)

    return encoded_data


def huffman_decode(path_in, path_out):
    with open(path_in, 'r', encoding='utf-8') as encoded_file:
        encoded_data = encoded_file.read()

    huffman_codes = {}
    with open('tests/codes.txt', 'r', encoding='utf-8') as codes_file:
        for line in codes_file:
            line = line.strip()
            if ': ' in line:
                symbol, code = line.split(': ', 1)
                huffman_codes[symbol] = code

    reversed_codes = {v: k for k, v in huffman_codes.items()}

    decoded_data = []
    buffer = ""

    for bit in encoded_data:
        buffer += bit
        if buffer in reversed_codes:
            decoded_data.append(reversed_codes[buffer])
            buffer = ""

    decoded_string = ''.join(decoded_data)
    decoded_string = decoded_string.replace('<SPACE>', ' ').replace('<NEWLINE>', '\n')

    with open(path_out, 'w', encoding='utf-8') as decoded_file:
        decoded_file.write(decoded_string)

    return decoded_string


def generate_canonical_codes(huffman_codes):
    sorted_codes = sorted(huffman_codes.items(), key=lambda item: (len(item[1]), item[0]))
    canonical_codes = {}

    current_code = 0
    code_length = 1

    for symbol, _ in sorted_codes:
        while len(bin(current_code)) - 2 > code_length:
            code_length += 1
            current_code = current_code >> 1

        canonical_codes[symbol] = format(current_code, f'0{code_length}b')
        current_code += 1

    return canonical_codes


def generate_canonical_codes_by_length(lengths):
    canonical_codes = []
    code = 0
    for length in sorted(set(lengths)):
        for _ in range(1 << (length - 1)):
            canonical_codes.append(format(code, f'0{length}b'))
            code += 1
        code <<= 1
    return canonical_codes
