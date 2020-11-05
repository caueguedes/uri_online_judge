n = int(input())

remaining_list = [x for x in range(1, 10001) if x % n == 2]

print(*remaining_list, sep='\n')
