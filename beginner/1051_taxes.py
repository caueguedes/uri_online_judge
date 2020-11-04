salary = float(input())
taxes = 0

if salary > 4500:
    rest = salary - 4500
    taxes += rest * 0.28
    salary = 4500
if salary > 3000:
    rest = salary - 3000
    taxes += rest * 0.18
    salary = 3000
if salary > 2000:
    rest = salary - 2000
    taxes += rest * 0.08

if taxes == 0:
    print('Isento')
else:
    print("R$ {:.2f}".format(taxes))
