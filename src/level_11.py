from PIL import Image


def solution(picture_filename: str):
    with Image.open(f"data/{picture_filename}") as im:
        pixels = im.load()
        width, height = im.size

        even_img = Image.new("RGB", (width // 2, height // 2))

        for i in range(width):
            for j in range(height):
                if i % 2 == 0 and j % 2 == 0:
                    even_img.putpixel((i // 2, j // 2), pixels[i, j])

        even_img.show()


solution("cave.jpg")
