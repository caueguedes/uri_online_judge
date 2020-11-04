positives = 0

for x in range(6):
    value = float(input())
    if value >= 0:
        positives += 1

print(f"{positives} valores positivos")