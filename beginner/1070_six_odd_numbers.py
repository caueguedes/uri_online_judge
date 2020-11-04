number = int(input())

if number % 2 == 0:
    number += 1

for index in range(6):
    print(number + index * 2)
