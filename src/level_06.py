import re
from collections import Counter
from typing import Optional
from zipfile import ZipFile

import utils


def solution(zip_filename: str, initial_filename: str) -> str:
    with ZipFile(f"data/{zip_filename}", "r") as z:
        next_nothing = initial_filename
        comments = []

        while next_nothing:
            text = z.read(f"{next_nothing}.txt").decode("utf-8")
            comments.append(z.getinfo(f"{next_nothing}.txt").comment.decode("utf-8"))
            next_nothing = extract_next_nothing(text)

        # hint
        split_comments = "".join(comments).split("\n")
        print("ONE MORE HINT:")
        print("\n".join(split_comments))

        letters = Counter(comments)
        answer = [k.lower() for k in letters.keys() if k not in [" ", "*", "\n"]]
        return "".join(answer)


def get_hint(zip_filename: str, initial_filename: str, is_step_output=False) -> str:
    with ZipFile(f"data/{zip_filename}", "r") as z:
        text = ""
        next_nothing = initial_filename

        while next_nothing:
            text = z.read(f"{next_nothing}.txt").decode("utf-8")
            if is_step_output:
                print(text)
            next_nothing = extract_next_nothing(text)

        return text


def get_readme(zip_filename: str) -> str:
    with ZipFile(f"data/{zip_filename}", "r") as z:
        text = z.read("readme.txt").decode("utf-8")
        return text


def extract_next_nothing(text: str) -> Optional[str]:
    matches = re.findall(r"Next nothing is (\d+)", text)
    return matches[0] if matches else None


filename = "channel.zip"

readme = get_readme(filename)
print(f"README:\n{readme}\n----------------------")

hint = get_hint(filename, initial_filename="90052")
print(f"HINT:\n{hint}\n----------------------")

sol = solution(filename, initial_filename="90052")
utils.print_solution_html(sol)

