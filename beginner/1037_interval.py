valor = float(input())


def intervalo(valor):
    if round(valor, 2) < 0 or round(valor, 2) > 100:
        return "Fora de intervalo"
    if round(valor, 2) <= 25:
        return "Intervalo [0,25]"
    if round(valor, 2) <= 50:
        return "Intervalo (25,50]"
    if round(valor, 2) <= 75:
        return "Intervalo (50,75]"
    else:
        return "Intervalo (75,100]"


resultado = intervalo(valor)
print(resultado)