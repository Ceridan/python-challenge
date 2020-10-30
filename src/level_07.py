import re

from PIL import Image

import utils


def solution(picture_filename: str) -> str:
    with Image.open(f"data/{picture_filename}") as im:
        pixels = im.load()
        width, height = im.size
        grey_row = []
        prev_pixel = (0, 0, 0)

        for w in range(width):
            r, g, b, _ = pixels[w, height // 2]
            if r == g and g == b:
                if prev_pixel != (r, g, b):
                    grey_row.append(chr(r))
                    prev_pixel = (r, g, b)

        hint = "".join(grey_row)
        print(hint)

        cipher = [int(x) for x in re.findall(r"(\d+)", hint)]
        result = [chr(x) if x >= 100 else chr(x + 100) for x in cipher]
        return "".join(result)


sol = solution("oxygen.png")
utils.print_solution_html(sol)
