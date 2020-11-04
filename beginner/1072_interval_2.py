times = repetitions = int(input())
in_interval = 0

while repetitions > 0:
    repetitions -= 1
    number = int(input())

    if 21 > number > 9:
        in_interval += 1

print(f"{in_interval} in")
print(f"{times - in_interval} out")
