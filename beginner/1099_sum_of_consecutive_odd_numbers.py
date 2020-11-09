iterations = int(input())

while iterations > 0:
    iterations -= 1

    value_1, value_2 = map(int, input().split())
    if value_1 > value_2:
        value_1, value_2 = value_2, value_1

    values = [value for value in range(value_1 + 1, value_2) if value % 2 == 1]
    print(sum(values))
