number = 0
iterations = 3


def print_number():
    global number
    print(number)
    number = 0


while iterations > 0:
    option = input()

    if option == "caw caw":
        iterations -= 1
        print_number()
    else:
        option = ['1' if character == '*' else '0' for character in option]
        number += int(''.join(option), 2)



