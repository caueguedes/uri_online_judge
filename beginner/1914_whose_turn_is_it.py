iterations = int(input())

for _ in range(iterations):
    player1, choice1, player2, choice2 = input().split()
    values = map(int, input().split())

    even = sum(values) % 2

    if even:
        if choice1 == "IMPAR":
            print(player1)
        else:
            print(player2)
    else:
        if choice1 == "PAR":
            print(player1)
        else:
            print(player2)
