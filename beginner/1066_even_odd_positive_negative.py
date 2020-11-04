values = {'even': 0, 'odd': 0, 'positive': 0, 'negative': 0}
for x in range(5):
    number = int(input())
    if number > 0:
        values['positive'] += 1
    if number < 0:
        values['negative'] += 1
    if number % 2 == 0:
        values['even'] += 1
    else:
        values['odd'] += 1

formatted = """{} valor(es) par(es)
{} valor(es) impar(es)
{} valor(es) positivo(s)
{} valor(es) negativo(s)""".format(values['even'], values['odd'],
                                   values['positive'], values['negative'])
print(formatted)
