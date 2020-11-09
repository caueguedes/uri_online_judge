iterations = int(input())

for index in range(1, iterations+1):
    square = index**2
    cubic = index**3
    print("{} {} {}".format(index, square, cubic))
    print("{} {} {}".format(index, square+1, cubic+1))