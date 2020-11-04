value = int(input())

odd_numbers = [number for number in range(value+1) if number % 2 == 1]
print(*odd_numbers, sep="\n")
