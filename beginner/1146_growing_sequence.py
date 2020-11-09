while True:
    value = int(input())
    if value == 0:
        break
    print(*[value for value in range(1, value+1)])