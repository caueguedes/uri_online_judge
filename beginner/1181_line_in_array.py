line = int(input())
operation = input()

start_line = line * 12 - 1
end_line = (line + 1) * 12
values = []

for index in range(144):
    value = float(input())

    if end_line > index > start_line:
        values.append(value)

if operation == 'S':
    print(f"{sum(values):.1f}")
else:
    average = sum(values) / len(values)
    print(f"{average:.1f}")
