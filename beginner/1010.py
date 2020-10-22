product, units, price = input().split(' ')
total = int(units) * float(price)

product, units, price = input().split(' ')
total += int(units) * float(price)

print("VALOR A PAGAR: R$ %.2f" % total)
