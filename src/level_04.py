import http.client
import re
from typing import Optional

import utils


def solution(initial_nothing: int) -> str:
    conn = http.client.HTTPConnection("www.pythonchallenge.com")
    try:
        next_nothing = str(initial_nothing)
        while next_nothing:
            conn.request("GET", f"/pc/def/linkedlist.php?nothing={next_nothing}")
            res = conn.getresponse()
            print(res.status, res.reason)
            text = res.read().decode("utf-8")
            print(text)
            next_nothing = extract_next_nothing(text)
        return text
    finally:
        conn.close()


def extract_next_nothing(text: str) -> Optional[str]:
    matches = re.findall(r"next nothing is (\d+)", text)
    return matches[0] if matches else None


hint = solution(12345)
sol = solution(16044 // 2)
utils.print_solution(sol)
