values = []

for x in range(6):
    value = float(input())
    values.append(value)

positives = [x for x in values if x >= 0]
average = sum(positives)/len(positives)

formatted_string = """{:d} valores positivos
{:.1f}""".format(len(positives), average)
print(formatted_string)
