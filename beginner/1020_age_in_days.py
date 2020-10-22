age = int(input())
year = age // 365
month = age % 365 // 30
day = age % 365 % 30

formatted = f"""{year} ano(s)
{month} mes(es)
{day} dia(s)"""

print(formatted)