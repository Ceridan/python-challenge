from typing import List

import utils


def solution() -> int:
    val = []
    seq = generate_sequence()
    for i in range(31):
        val = next(seq)
    return len(val)


def generate_sequence() -> List[int]:
    current = [1]
    yield current

    while True:
        nxt = []
        x = current[0]
        cnt = 1
        for i in range(1, len(current)):
            if x != current[i]:
                nxt.append(cnt)
                nxt.append(x)
                x = current[i]
                cnt = 1
            else:
                cnt += 1
        nxt.append(cnt)
        nxt.append(x)
        yield nxt
        current = nxt


sol = solution()
print("Sequence: a = [1, 11, 21, 1211, 111221, ... ]. len(a[30])?")
utils.print_solution_return_html(str(sol))
