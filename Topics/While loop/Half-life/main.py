HALF_LIFE_IN_DAYS = 12
initial_quantity = int(input().strip())
final_quantity = int(input().strip())

half_lives = 0
while initial_quantity >= final_quantity:
    half_lives += 1
    initial_quantity //= 2
print(half_lives * HALF_LIFE_IN_DAYS)
