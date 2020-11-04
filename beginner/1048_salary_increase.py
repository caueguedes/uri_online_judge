salary = float(input())


def percentage_adjustment(salary):
    if salary <= 400:
        return 0.15
    if salary <= 800:
        return 0.12
    if salary <= 1200:
        return 0.1
    if salary <= 2000:
        return 0.07
    return 0.04


percentage = percentage_adjustment(salary)
readjustment = salary * percentage
new_salary = salary + readjustment

formatted = """Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: {:d} %"""

print(formatted.format(new_salary, readjustment, int(percentage*100)))
