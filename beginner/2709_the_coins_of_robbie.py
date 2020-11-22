import sys
sys.stdout = open(sys.stdout.buffer.fileno(), 'w', encoding='utf8')


def prime_number(value):
    divisors = 0

    for divisor in range(2, value//2 + 1):
        if value % divisor == 0:
            divisors += 1

    if divisors:
        return False
    return True


while True:
    try:
        size = int(input())

        coins = []
        for _ in range(size):
            coin = int(input())
            coins.append(coin)

        frequency = int(input())
        coins = [coin for index, coin in enumerate(reversed(coins)) if index % frequency == 0]
        coins_total = sum(coins)

        if prime_number(coins_total):
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")

    except EOFError:
        break
