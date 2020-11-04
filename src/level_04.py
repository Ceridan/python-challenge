import re
from typing import Optional

import requests

import utils


def solution(initial_nothing: int) -> str:
    text = ""
    next_nothing = str(initial_nothing)

    while next_nothing:
        r = requests.get(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={next_nothing}")
        print(f"{r.status_code} {r.reason}: {r.text}")
        text = r.text
        next_nothing = extract_next_nothing(text)
    return text


def extract_next_nothing(text: str) -> Optional[str]:
    matches = re.findall(r"next nothing is (\d+)", text)
    return matches[0] if matches else None


hint = solution(12345)
sol = solution(16044 // 2)
utils.print_solution(sol)
