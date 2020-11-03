values = list(map(int, input().split()))

sorted = values.copy()
sorted.sort()

print(*sorted, sep="\n")
print("")
print(*values, sep="\n")