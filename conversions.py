from PIL import Image
import numpy as np


def png_to_raw(image_path, output_path):
    image = Image.open(image_path)
    if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
        image = image.convert('RGB')

    raw_pixels = np.array(image)
    raw_data = raw_pixels.tobytes()

    # binary_data = ' '.join(format(byte, '08b') for byte in raw_data)
    # print(binary_data)

    with open(output_path, 'wb') as f:
        f.write(raw_data)
        return raw_data
