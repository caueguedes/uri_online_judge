iterations = int(input())

while iterations > 0:
    iterations -= 1

    value, times = map(int, input().split())

    if value % 2 == 0:
        value += 1

    stop_value = value + 2 * (times - 1)
    values = [value for value in range(value, stop_value + 1, 2)]

    summed_value = sum(values)
    print(summed_value)