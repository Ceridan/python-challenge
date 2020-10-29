import utils
import re


def solution(data: str) -> str:
    result = re.findall(r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", data)
    return "".join(result)


input_data = utils.read_input_from_file(level=3)
sol = solution(input_data)
utils.print_solution_php(sol)
