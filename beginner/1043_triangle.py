a, b, c = map(float, input().split())

if a+b <= c or a+c <= b or b+c <= a:
    area = (a + b)/2 * c
    print("Area = {:.1f}".format(area))
else:
    perimetro = a + b + c
    print("Perimetro = {:.1f}".format(perimetro))
