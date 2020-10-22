from math import sqrt

x1, y1 = map(float, input().split(" "))
x2, y2 = map(float, input().split(" "))

x = x2 - x1
x = x**2
y = y2 - y1
y = y**2

distance = sqrt(x+y)

print("%.4f" % distance)
