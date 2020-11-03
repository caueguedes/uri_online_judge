def eixo(x, y):
    if x == 0:
        if y == 0:
            return "Origem"
        else:
            return "Eixo Y"
    else:
        if y == 0:
            return "Eixo X"

    if x > 0:
        if y > 0:
            return "Q1"
        else:
            return "Q4"
    else:
        if y > 0:
            return "Q2"
        else:
            return "Q3"


x, y = map(float, input().split())

print(eixo(x, y))

