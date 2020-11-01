import matplotlib.pyplot as plt

import utils


def solution(first: str, second: str):
    dots1 = [int(x) for x in first.split(",")]
    dots2 = [int(x) for x in second.split(",")]

    img = plt.imread("data/good.jpg")
    _, ax = plt.subplots()
    ax.imshow(img)

    for dots in [dots1, dots2]:
        xs = [x for i, x in enumerate(dots) if i % 2 == 0]
        ys = [y for i, y in enumerate(dots) if i % 2 == 1]
        ax.plot(xs, ys, '-')

    plt.savefig("out/level_09.jpg")
    print("See result picture: \"out/level_09.jpg\"")


first_input = utils.read_file("data/level_09_01.txt")
second_input = utils.read_file("data/level_09_02.txt")
solution(first_input, second_input)
