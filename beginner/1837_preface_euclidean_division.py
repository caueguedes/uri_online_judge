a, b = map(int, input().split())


if b < 0:
    q = a // b if a % b == 0 else a // b + 1
else:
    q = a // b

r = a - q * b

print(q, r)
