from PIL import Image, ImageFile


def solution(gfx_filename: str):
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
