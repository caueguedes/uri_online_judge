iterations = 20
array = []

while iterations > 0:
    iterations -= 1

    value = int(input())
    array.append(value)

for index, value in enumerate(array[::-1]):
    print("N[{}] = {}".format(index, value))
