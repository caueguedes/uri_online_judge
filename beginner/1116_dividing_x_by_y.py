iterations = int(input())

while iterations > 0:
    iterations -= 1

    dividend, divisor = map(int, input().split())

    if divisor == 0:
        print('divisao impossivel')
    else:
        print("{:.1f}".format(dividend/divisor))
