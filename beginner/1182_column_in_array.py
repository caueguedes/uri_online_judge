column = int(input())
operation = input()

values = []

for index in range(144):
    value = float(input())

    if (index - column) % 12 == 0:
        values.append(value)

if operation == 'S':
    print(f"{sum(values):.1f}")
else:
    average = sum(values) / len(values)
    print(f"{average:.1f}")
