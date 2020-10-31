item, quantity = map(int, input().split())
items = [4.0, 4.5, 5.0, 2.0, 1.5]

total = items[item-1] * quantity
print("Total: R$ {:.2f}".format(total))