iterations = int(input())
animals = {'C': 0, 'R': 0, 'S': 0}

while iterations > 0:
    iterations -= 1

    quantity, animal = input().split()
    animals[animal] += int(quantity)

total = animals['C'] + animals['R'] + animals['S']

formatted = """Total: {} cobaias
Total de coelhos: {}
Total de ratos: {}
Total de sapos: {}
Percentual de coelhos: {:.2f} %
Percentual de ratos: {:.2f} %
Percentual de sapos: {:.2F} %""".format(
    total,
    animals['C'],
    animals['R'],
    animals['S'],
    animals['C']/total*100,
    animals['R']/total*100,
    animals['S']/total*100
)
print(formatted)
