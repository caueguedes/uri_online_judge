from math import sqrt

while True:
    operation = input()

    if len(operation) == 1:
        break
    else:
        a, b, c = map(int, operation.split())
        area = a*b
        rate = 100/c
        print(int(sqrt(area*rate)))

