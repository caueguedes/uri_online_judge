for i in range(1, 10, 2):
    print(*[f"I={i} J={j}" for j in range(i+6, i+3, -1)], sep='\n')
