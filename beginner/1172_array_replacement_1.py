iterations = 10
array = []

while iterations > 0:
    iterations -= 1

    value = int(input())
    value = value if value > 0 else 1
    array.append(value)

for index, value in enumerate(array):
    print("X[{}] = {}".format(index, value))