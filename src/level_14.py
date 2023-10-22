from PIL import Image


def solution(picture_filename: str):
    with Image.open(f"data/{picture_filename}") as img:
        pixels = img.load()
        width, height = 100, 100
        new_img = Image.new("RGB", (width, height))

        index, level = 0, 0
        for i in range(100, 1, -2):
            for j in range(i):
                new_img.putpixel((level + j, level), pixels[index, 0])
                index += 1

            for j in range(i - 1):
                new_img.putpixel((width - level - 1, level + j + 1), pixels[index, 0])
                index += 1

            for j in range(i - 1):
                new_img.putpixel((width - level - 1 - j, height - level - 1), pixels[index, 0])
                index += 1

            for j in range(i - 2):
                new_img.putpixel((level, height - level - 1 - j), pixels[index, 0])
                index += 1

            level += 1

        new_img.show()


solution("wire.png")
