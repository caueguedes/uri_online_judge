while True:
    value = int(input())

    if value == 0:
        break
    elif value % 2 == 1:
        value += 1

    stop_value = value + 2 * 4
    values = [value for value in range(value, stop_value + 1, 2)]

    summed_value = sum(values)
    print(summed_value)