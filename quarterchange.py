import get_float

while True:
    dollars = get_float("Change owed: ")
    if dollars >= 0:
        break

cents = round(dollars * 100)  # 41 -25 = 16 -10 = 6 - 5= 1
coins = 0  # 1 2 3
denominations = [25, 10, 5, 1]

for denom in denominations:
    while cents >= denom:
        cents -= denom
        coins += 1

print(coins)
