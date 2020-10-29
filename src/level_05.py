import os
import pickle
from typing import Tuple, List


def solution(filename: str):
    data = unpickling(filename)
    for row in data:
        line = "".join([ch * cnt for ch, cnt in row])
        print(line)


def unpickling(filename: str) -> List[List[Tuple[str, int]]]:
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, f"../data/{filename}")
    with open(file_path, "rb") as f:
        decoded = pickle.load(f, encoding="utf-8")
        return decoded


solution("banner.p")
