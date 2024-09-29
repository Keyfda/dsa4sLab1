def count_probability(data):
    num = 0
    sr = ""
    dictionary = []
    for i in data:
        if sr.count(i) == 0:
            k = data.count(i)
            num += k
            dictionary.append((i, k))
            sr += i
    dictionary.sort(key=lambda x: x[1], reverse=True)

    probability = []
    indices = {}
    k = 0

    for i in range(len(dictionary)):
        probability.append(dictionary[i][1] / num)
        indices[dictionary[i][0]] = k
        k += 1

    print("send to Arithmetic_probability.txt:\n1 - yes\n2 - no")
    f2 = int(input())
    if f2 == 1:
        with open("tests/texts/Arithmetic_probability.txt", "w", encoding="utf-8") as file:
            file.write("total=" + str(num) + chr(2))
            for i in range(len(dictionary)):
                file.write(dictionary[i][0] + '=' + str(dictionary[i][1]) + chr(2))

    return probability, indices


def read_probability(decode):  # Чтение вероятностей из файла
    with open("tests/texts/Arithmetic_probability.txt", "r", encoding="utf-8") as file:
        data = file.read()

    probability = []
    indices = {}
    sr = ""
    for i in data[6:]:
        if i != chr(2):
            sr += i
        else:
            break
    num = int(sr)
    ln = len(sr)
    sr = ""
    n = False
    k = 0
    sym = ''

    for i in data[7 + ln:]:
        if i == '=':
            n = True
        elif i != chr(2) and n:
            sr += i
        elif i == chr(2):
            n = False
            probability.append(int(sr) / num)
            sr = ""
            if decode:
                indices[k] = sym
                k += 1
        else:
            if decode:
                sym = i
            else:
                indices[i] = k
                k += 1
    return probability, indices


def ac_enc(path_in, path_out):
    with open(path_in, "r", encoding="utf-8") as file:
        data = file.read()

    print("choose probability:\n1 - use count_probability\n2 - read Arithmetic_probability.txt\n")
    f2 = int(input())
    if f2 == 1:
        probability, indices = count_probability(data)
    elif f2 == 2:
        probability, indices = read_probability(False)

    intervals = [sum(probability[:i]) for i in range(len(probability) + 1)]
    Left = 0
    Right = 1
    double_list = []
    num_list = []

    i = 0
    num = 0
    while i < len(data):
        length = Right - Left
        Left, Right = Left + intervals[indices[data[i]]] * length, Left + intervals[indices[data[i]] + 1] * length
        for j in range(len(indices)):
            L, R = Left + intervals[j] * length, Left + intervals[j + 1] * length
            if L == R:
              #  print("Error may occur")
                double_list.append((Left + Right) / 2)
                Left = 0
                Right = 1
                num_list.append(num)
                num = -1
                i -= 1
                break
        i += 1
        num += 1

    double_list.append((Left + Right) / 2)
    num_list.append(num)

    with open(path_out, "w", encoding="utf-8") as file2:
        for i in range(len(double_list)):
            file2.write(str(num_list[i]) + "," + str(double_list[i]) + ",")


def ac_dec(path_in, path_out):
    with open(path_in, "r", encoding="utf-8") as file:
        data = file.read()

    probability, indices = read_probability(True)
    sr = ""
    double_list = []
    num_list = []

    nm = True
    for i in data:
        if i != ",":
            sr += i
        elif nm:
            num_list.append(int(sr))
            sr = ""
            nm = False
        else:
            double_list.append(float(sr))
            sr = ""
            nm = True

    intervals = [sum(probability[:i]) for i in range(len(probability) + 1)]
    data2 = ""

    for c in range(len(double_list)):
        Left = 0
        Right = 1
        number = double_list[c]
        num = num_list[c]
        j = 0
        changing_intervals = intervals

        while Left != Right and j < num:
            index_interval = sum([number > i for i in changing_intervals]) - 1
            data2 += indices[index_interval]
            Left = changing_intervals[index_interval]
            Right = changing_intervals[index_interval + 1]
            length = Right - Left
            changing_intervals = [Left + length * intervals[i] for i in range(len(intervals))]
            j += 1

    with open(path_out, "w", encoding="utf-8") as file2:
        file2.write(data2)
