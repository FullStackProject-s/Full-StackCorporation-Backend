from io import BytesIO
from PIL import ImageDraw, Image

from django.core.files.base import ContentFile

import random
import numpy as np
import hashlib


def generate_avatar(*args, avatar_size: int = 12 * 35) -> ContentFile:
    """
    Take str args unique string value, minimum 1
    and optional avatar_size value multiple of 12
    """
    background_color = '#f2f1f2'
    random_string = args[0] + str(random.randbytes(10))

    sha = hashlib.sha256(str(hex(sum(hash(ele) for ele in args))).encode())

    hex_number = sha.hexdigest()

    color = '#' + hex_number[2:8]

    bytes_ = hashlib.md5(random_string.encode('utf-8')).digest()

    need_color = np.array(
        [bit == '1' for byte in bytes_[3:3 + 9] for bit in
         bin(byte)[2:].zfill(8)]
    ).reshape(6, 12)

    need_color = np.concatenate((need_color, need_color[::-1]), axis=0)

    for i in range(12):
        need_color[0, i] = 0
        need_color[11, i] = 0
        need_color[i, 0] = 0
        need_color[i, 11] = 0

    img_size = (avatar_size, avatar_size)
    block_size = avatar_size // 12

    img = Image.new('RGB', img_size, background_color)
    draw = ImageDraw.Draw(img)

    for x in range(avatar_size):
        for y in range(avatar_size):
            need_to_paint = need_color[x // block_size, y // block_size]
            if need_to_paint:
                draw.point((x, y), color)

    buffer = BytesIO()
    img.save(fp=buffer, format='PNG')
    return ContentFile(buffer.getvalue())
