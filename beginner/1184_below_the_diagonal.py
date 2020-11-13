operation = input()

values = []
for line in range(12):
    for column in range(12):
        value = float(input())

        if column + line < 11:
            values.append(value)

if operation == 'S':
    print(f"{sum(values):.1f}")
else:
    average = sum(values) / len(values)
    print(f"{average:.1f}")
