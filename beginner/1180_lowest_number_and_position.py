_ = input()

values = list(map(int, input().split()))

min_value = min(values)
index = values.index(min_value)

print("""Menor valor: {}
Posicao: {}""".format(min_value, index))
