ages = []
while True:
    age = int(input())
    if age <= 0:
        break
    ages.append(age)

average = sum(ages) / len(ages)
print("{:.2f}".format(average))
