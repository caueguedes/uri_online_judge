iterations = 100
values_list = []

while iterations > 0:
    iterations -= 1
    value = int(input())
    values_list.append(value)

highest = max(values_list)
index = values_list.index(highest)

print(*[highest, index+1], sep='\n')