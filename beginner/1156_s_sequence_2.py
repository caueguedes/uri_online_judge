values = [value/2**(value//2) for value in range(3, 40, 2)]

amount = sum(values) + 1
print("{:.2f}".format(amount))