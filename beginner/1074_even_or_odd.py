iterations = int(input())

while iterations > 0:
    iterations -= 1

    value = int(input())
    if value == 0:
        print('NULL')
        continue

    if value % 2 == 0:
        print('EVEN', end=' ')
    else:
        print('ODD', end=' ')

    if value > 0:
        print('POSITIVE')
    else:
        print('NEGATIVE')
