day1, day2, day3 = map(int, input().split())


def check_temperature():
    # decreased
    if day1 > day2:
        if day2 <= day3:
            return ":)"

        if day2 > day3:
            return ":)" if day1-day2 > day2-day3 else ":("

    # increased
    elif day1 < day2:
        # decreased less or equal
        if day2 >= day3:
            return ":("

        # increased
        if day2 < day3:
            return ":(" if day2-day1 > day3-day2 else ":)"

    return ":)" if day2 < day3 else ":("


print(check_temperature())
