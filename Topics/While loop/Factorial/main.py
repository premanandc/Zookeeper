n = int(input().strip())

i = 1
factorial = 1
while i <= n:
    factorial *= i
    i += 1
print(factorial)
