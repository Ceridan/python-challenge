import requests
from PIL import Image, ImageFile


def solution(gfx_filename: str):
    r = requests.get(f"http://www.pythonchallenge.com/pc/return/evil4.jpg", auth=("huge", "file"))
    hint1 = r.text
    print(hint1)

    with open(gfx_filename, "rb") as evil_gfx:
        data = evil_gfx.read()
        for i in range(5):
            with open(f"out/evil{i + 1}.jpg", "wb") as raw:
                raw.write(data[i::5])

        ImageFile.LOAD_TRUNCATED_IMAGES = True
        for i in range(5):
            with Image.open(f"out/evil{i + 1}.jpg") as img:
                img.show()


solution("data/evil2.gfx")
