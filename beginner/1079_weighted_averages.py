iterations = int(input())

while iterations > 0:
    iterations -= 1

    val_1, val_2, val_3 = map(float, input().split())
    average = val_1 * 2 + val_2 * 3 + val_3 * 5
    average /= 10
    print(round(average, 1))
