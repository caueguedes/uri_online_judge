c, b, a = sorted(map(float, input().split()))


def which_triangle(a, b, c):
    text = []
    if a >= b + c:
        text.append("NAO FORMA TRIANGULO")
        return text
    if a**2 == b**2 + c**2:
        text.append("TRIANGULO RETANGULO")
    if a**2 > b**2 + c**2:
        text.append("TRIANGULO OBTUSANGULO")
    if a**2 < b**2 + c**2:
        text.append("TRIANGULO ACUTANGULO")
    if a == b and b == c:
        text.append("TRIANGULO EQUILATERO")
    if a == b != c or a != b == c:
        text.append("TRIANGULO ISOSCELES")
    return text


print(*which_triangle(a, b, c), sep='\n')
