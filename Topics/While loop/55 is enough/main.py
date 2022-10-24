# put your code here
MAGIC_NUMBER = 55

how_many = 0
total = 0

n = int(input().strip())
while n != MAGIC_NUMBER:
    how_many += 1
    total += n
    n = int(input().strip())
print(how_many, total, round(total / how_many), sep='\n')
