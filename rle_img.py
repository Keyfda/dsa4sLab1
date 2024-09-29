import numpy as np
import conversions as conv


def rle_img_enc(file_path, output_path):
    raw_data = conv.png_to_raw(file_path, output_path)
    flat_pixels = np.frombuffer(raw_data, dtype=np.uint8)

    rle_data = bytearray()
    count = 1

    for i in range(1, len(flat_pixels)):
        if flat_pixels[i] == flat_pixels[i - 1]:
            count += 1
            if count == 255:
                rle_data.append(count)
                rle_data.append(flat_pixels[i - 1])
                count = 0
        else:
            if count > 0:
                rle_data.append(count)
                rle_data.append(flat_pixels[i - 1])
            count = 1

    if count > 0:
        rle_data.append(count)
        rle_data.append(flat_pixels[-1])

    with open(output_path, 'wb') as f:
        f.write(rle_data)


def rle_img_dec(encoded_file_path, output_raw_path):
    with open(encoded_file_path, 'rb') as f:
        rle_data = f.read()

    flat_pixels = bytearray()
    i = 0
    while i < len(rle_data):
        count = rle_data[i]
        pixel_value = rle_data[i + 1]
        flat_pixels.extend([pixel_value] * count)
        i += 2

    with open(output_raw_path, 'wb') as f:
        f.write(flat_pixels)
