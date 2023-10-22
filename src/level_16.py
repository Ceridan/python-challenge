from PIL import Image


def solution(picture_filename: str):
    pink_pixel = 195

    with Image.open(f"data/{picture_filename}") as img:
        pixels = img.load()
        new_img = Image.new("RGB", (img.width, img.height))
        for h in range(img.height):
            pos = -1
            for w in range(img.width):
                if pos == -1 and (pixels[w, h]) == pink_pixel:
                    pos = w
                if pos > -1:
                    new_img.putpixel((w - pos, h), pixels[w, h])
            for w in range(pos):
                new_img.putpixel((w + img.width - pos, h), pixels[w, h])
        new_img.show()


solution("mozart.gif")
