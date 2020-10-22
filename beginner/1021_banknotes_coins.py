notes = float(input())
notes_coins = []


for value in [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]:
    notes_coins.append(int(notes // value))
    notes = notes % value

formatted = """NOTAS:
{} nota(s) de R$ 100.00
{} nota(s) de R$ 50.00
{} nota(s) de R$ 20.00
{} nota(s) de R$ 10.00
{} nota(s) de R$ 5.00
{} nota(s) de R$ 2.00
MOEDAS:
{} moeda(s) de R$ 1.00
{} moeda(s) de R$ 0.50
{} moeda(s) de R$ 0.25
{} moeda(s) de R$ 0.10
{} moeda(s) de R$ 0.05
{} moeda(s) de R$ 0.01"""

formatted = formatted.format(notes_coins)
print(formatted)