init = int(input())
end = int(input())

if init > end:
    init, end = end, init

numbers = [value for value
             in range(init+1, end)
             if value % 5 == 2 or value % 5 == 3]

print(*numbers, sep="\n")