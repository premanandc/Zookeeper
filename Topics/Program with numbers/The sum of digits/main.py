# put your python code here
n = int(input())

h = n // 100
t = (n - h * 100) // 10
o = n % 10
print(h + t + o)
