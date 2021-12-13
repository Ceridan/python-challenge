import datetime


def solution() -> str:
    dates = []

    for year in range(1000, 2000):
        year_str = str(year)

        if year_str[0] == "1" and year_str[-1] == "6" and is_leap_year(year):
            dt = datetime.date(year, 1, 26)
            if dt.weekday() == 0:
                dates.append(dt)

    second = dates[-2]
    return f"{second.year}-{str(second.month).zfill(2)}-{str(second.day + 1).zfill(2)}"


def is_leap_year(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0:
        return True

    if year % 400 == 0:
        return True

    return False


sol = solution()
print(sol)  # Wolfgang Amadeus Mozart (27 January 1756 – 5 December 1791)
