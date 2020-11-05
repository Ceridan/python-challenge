import xmlrpc.client

import utils


def solution() -> str:
    with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as proxy:
        hint1 = proxy.phone("evil")
        print(f"Phone that evil (hint 1, see hint on previous level): {str(hint1)}")
        hint2 = proxy.phone("Bert")
        print(f"Phone that evil (hint 2): {str(hint2)}")
        return hint2.replace("555-", "").lower()


sol = solution()
utils.print_solution_return_html(sol)
