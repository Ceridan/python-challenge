import utils


def solution(cipher: str) -> str:
    original = []

    for ch in cipher:
        if ch.isalpha():
            new_ch = chr((ord(ch) - 97 + 2) % 26 + 97)
            original.append(new_ch)
        else:
            original.append(ch)

    return "".join(original)


input_cipher = utils.read_input_from_file(level=1)
hint = solution(input_cipher)
print(hint)

sol = solution("map")
utils.print_solution(sol)
