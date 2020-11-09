factor_number = int(input())

factorial_value = 1
for number in range(1, factor_number+1):
    factorial_value *= number

print(factorial_value)