a, b, c = map(float, input().split(' '))

triangle = a * c / 2
circle = c**2 * 3.14159
trapezium = (a + b) / 2 * c
square = b ** 2
rectangle = a * b

print("TRIANGULO: %.3f" % triangle)
print("CIRCULO: %.3f" % circle)
print("TRAPEZIO: %.3f" % trapezium)
print("QUADRADO: %.3f" % square)
print("RETANGULO: %.3f" % rectangle)
