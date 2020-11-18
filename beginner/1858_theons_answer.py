_ = input()

persons = list(map(int, input().split()))

min_value = min(persons)
print(persons.index(min_value)+1)
