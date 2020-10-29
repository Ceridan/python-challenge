import os


def read_input_from_file(level: int) -> str:
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, f"../data/level_{str(level).zfill(2)}.txt")
    with open(file_path) as f:
        return f.read()


def print_solution(solution: str) -> str:
    print(f"http://www.pythonchallenge.com/pc/def/{solution}.html")
