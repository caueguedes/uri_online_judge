per_line, max_value = map(int, input().split())
index = 1

while index <= max_value:
    values = [value for value in range(index, index+per_line) if value <= max_value]
    print(*values)
    index += per_line

