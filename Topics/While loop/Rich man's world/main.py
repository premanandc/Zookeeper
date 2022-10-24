MAX_PRINCIPAL = 700000
principal = float(input().strip())
RATE = 7.1

years = 1
amount = principal * (1 + RATE / 100) ** years
while amount < MAX_PRINCIPAL:
    years += 1
    amount = principal * (1 + RATE / 100) ** years
print(years)
