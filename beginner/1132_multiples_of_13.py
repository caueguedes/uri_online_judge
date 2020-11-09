init = int(input())
end = int(input())

if init > end:
    init, end = end, init

multiples = [value for value in range(init, end+1) if value % 13 != 0]

summed_multiples = sum(multiples)
print(summed_multiples)
