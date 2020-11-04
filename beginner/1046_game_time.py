start, end = map(int, input().split())

if start == end:
    print("O JOGO DUROU 24 HORA(S)")
else:
    duration = (24 - start + end) % 24
    print(f"O JOGO DUROU {duration} HORA(S)")
