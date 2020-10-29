import os


def read_input_from_file(level: int) -> str:
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, f"../data/level_{str(level).zfill(2)}.txt")
    with open(file_path) as f:
        return f.read()


def print_solution(solution: str) -> str:
    _print_solution_base(solution)


def print_solution_html(solution: str) -> str:
    _print_solution_base(f"{solution}.html")


def print_solution_php(solution: str) -> str:
    _print_solution_base(f"{solution}.php")


def _print_solution_base(solution_with_extension: str) -> str:
    print(f"Next level: http://www.pythonchallenge.com/pc/def/{solution_with_extension}")
