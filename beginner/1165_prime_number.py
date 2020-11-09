iterations = int(input())

while iterations > 0:
    iterations -= 1

    number = int(input())

    divisors = [divisor for divisor in range(1, number//2+1) if number % divisor == 0]

    if len(divisors) > 1:
        print("{} nao eh primo".format(number))
    else:
        print("{} eh primo".format(number))
