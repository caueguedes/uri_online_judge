x_value = int(input())

while True:
    z_value = int(input())
    if z_value > x_value:
        break

iterations = 0
amount = 0
while amount < z_value:
    amount += x_value + iterations
    iterations += 1

print(iterations)
