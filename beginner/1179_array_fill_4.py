even = []
odd = []


def print_even():
    for index, value in enumerate(even):
        print("par[{}] = {}".format(index, value))
    even.clear()


def print_odd():
    for index, value in enumerate(odd):
        print("impar[{}] = {}".format(index, value))
    odd.clear()


for _ in range(15):
    value = int(input())

    if value % 2 == 0:
        even.append(value)
    else:
        odd.append(value)

    if len(even) == 5:
        print_even()

    if len(odd) == 5:
        print_odd()


print_odd()
print_even()