fuel = {1: 0, 2: 0, 3: 0}

while True:
    type_of_fuel = int(input())

    if 0 < type_of_fuel < 4:
        fuel[type_of_fuel] += 1

    if type_of_fuel == 4:
        break


formatted_string = """MUITO OBRIGADO
Alcool: {}
Gasolina: {}
Diesel: {}""".format(fuel[1], fuel[2], fuel[3])
print(formatted_string)

