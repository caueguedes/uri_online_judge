start = int(input())
end = int(input())

if start > end:
    start, end = end, start

values = [value for value in range(start+1, end) if value % 2 == 1]
summed_values = sum(values)

print(summed_values)