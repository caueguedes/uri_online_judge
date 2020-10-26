from math import sqrt
a, b, c = map(float, input().split())

delta = b**2 - 4*a*c

if delta <= 0 or a == 0:
    print("Impossivel calcular")
else:
    sqrt_delta = sqrt(delta)
    divisor = 2 * a

    root_plus = -b + sqrt_delta
    root_plus /= divisor

    root_minus = -b - sqrt_delta
    root_minus /= divisor

    print("R1 = {:.5f}".format(root_plus))
    print("R2 = {:.5f}".format(root_minus))
