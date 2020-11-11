fibonacci = [0, 1]
while True:
    nex_value = fibonacci[-1] + fibonacci[-2]

    if len(bin(nex_value)) >= 65:
        break
    fibonacci.append(nex_value)


iterations = int(input())

for _ in range(iterations):
    value = int(input())
    print("Fib({}) = {}".format(value, fibonacci[value]))