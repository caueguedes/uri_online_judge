def bigger(a, b):
    return (a + b + abs(a - b))/2


a, b, c = map(int, input().split(' '))
val = bigger(a, b)
val = bigger(val, c)
print("%i eh o maior" % val)
