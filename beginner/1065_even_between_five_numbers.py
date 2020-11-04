times = 5
even_numbers = 0

while times > 0:
    value = int(input())
    if value % 2 == 0:
        even_numbers += 1
    times -= 1

print(f"{even_numbers} valores pares")

# OR
numbers = []
for x in range(5):
    number = int(input())
    numbers.append(number)

even_numbers = len([x for x in numbers if x % 2 == 0])
print(f"{even_numbers} valores pares")
