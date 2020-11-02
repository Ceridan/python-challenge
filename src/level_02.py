from collections import Counter

import utils


def solution(data: str) -> str:
    cnt = Counter(data)
    unique_chars = [k for k, v in cnt.items() if v == 1]
    return "".join(unique_chars)


input_data = utils.read_level_input_from_file(level=2)
sol = solution(input_data)
utils.print_solution_def_html(sol)
