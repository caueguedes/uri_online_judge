value = float(input())

for index in range(100):
    print("N[{}] = {:.4f}".format(index, value))
    value /= 2
