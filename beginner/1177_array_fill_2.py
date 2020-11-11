limit_value = int(input())

values = (value % limit_value for value in range(1000))

for index, value in enumerate(values):
    print("N[{}] = {}".format(index, value))
