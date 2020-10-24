import string


def plus_three(char):
    if char in string.ascii_letters:
        return ord(char) + 3
    else:
        return ord(char)


n_times = int(input())

for i in range(n_times):
    input_string = input()
    input_string = list(map(plus_three, input_string))
    input_string.reverse()

    half_string = (len(input_string) // 2)
    for char in range(half_string, len(input_string)):
        input_string[char] -= 1
    input_string = map(chr, input_string)
    print("".join(list(input_string)))
