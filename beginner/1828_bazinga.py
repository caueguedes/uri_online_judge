iterations = int(input())


def check_winner(hand1, hand2):
    if hand1 == "tesoura":
        if hand2 in ["papel", "lagarto"]:
            return True
    elif hand1 == "papel":
        if hand2 in ["pedra", "Spock"]:
            return True
    elif hand1 == "pedra":
        if hand2 in ["lagarto", "tesoura"]:
            return True
    elif hand1 == "lagarto":
        if hand2 in ["Spock", "papel"]:
            return True
    elif hand1 == "Spock":
        if hand2 in ["tesoura", "pedra"]:
            return True
    return False


for index in range(iterations):
    hand1, hand2 = input().split()
    if check_winner(hand1, hand2):
        print(f"Caso #{index + 1}: Bazinga!")
    elif hand1 == hand2:
        print(f"Caso #{index + 1}: De novo!")
    else:
        print(f"Caso #{index + 1}: Raj trapaceou!")
