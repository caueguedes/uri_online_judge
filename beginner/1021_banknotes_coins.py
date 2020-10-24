notes = float(input())
notes_coins = []

for value in [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]:
    quantity = int(round(notes,10) / round(value, 10))
    notes_coins.append(quantity)
    notes -= quantity * value

formatted = """NOTAS:
{:d} nota(s) de R$ 100.00
{:d} nota(s) de R$ 50.00
{:d} nota(s) de R$ 20.00
{:d} nota(s) de R$ 10.00
{:d} nota(s) de R$ 5.00
{:d} nota(s) de R$ 2.00
MOEDAS:
{:d} moeda(s) de R$ 1.00
{:d} moeda(s) de R$ 0.50
{:d} moeda(s) de R$ 0.25
{:d} moeda(s) de R$ 0.10
{:d} moeda(s) de R$ 0.05
{:d} moeda(s) de R$ 0.01"""

formatted = formatted.format(*notes_coins)
print(formatted)
