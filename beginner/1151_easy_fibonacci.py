length = int(input())
fibonacci = [0, 1]

for index in range(length):
    if index > 1:
        fibonacci.append(fibonacci[index-2]+fibonacci[index-1])

print(*fibonacci[: length])

