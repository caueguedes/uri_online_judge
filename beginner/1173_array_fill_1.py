iterations = 10
array = []

start = int(input())

while iterations > 0:
    iterations -= 1

    array.append(start)
    start *= 2

for index, value in enumerate(array):
    print("N[{}] = {}".format(index, value))
