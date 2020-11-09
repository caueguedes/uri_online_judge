values = input().split()
a, n = int(values[0]), int(values[-1])

values_list = [value + a for value in range(n)]
summed_values = sum(values_list)

print(summed_values)