amount = int(input())
hundred = amount // 100
fifty = amount % 100 // 50
twenty = amount % 100 % 50 // 20
ten = amount % 100 % 50 % 20 // 10
five = amount % 100 % 50 % 20 % 10 // 5
two = amount % 100 % 50 % 20 % 10 % 5 // 2
one = amount % 100 % 50 % 20 % 10 % 5 % 2

template = f"""{amount}
{hundred} nota(s) de R$ 100,00
{fifty} nota(s) de R$ 50,00
{twenty} nota(s) de R$ 20,00
{ten} nota(s) de R$ 10,00
{five} nota(s) de R$ 5,00
{two} nota(s) de R$ 2,00
{one} nota(s) de R$ 1,00"""
print(template)
