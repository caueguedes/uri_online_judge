iterations = 0

while iterations < 100:
    value = float(input())
    if value <= 10:
        print("A[{}] = {:.1f}".format(iterations, value))

    iterations += 1
