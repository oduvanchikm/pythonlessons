# 1var

x = int(input())
y = int(input())

x3 = x % 10
x2 = (x // 10) % 10
x1 = (x // 100) % 10

y3 = y % 10
y2 = (y // 10) % 10
y1 = (y // 100) % 10

v3 = str(x3 + y3)[-1]
v2 = str(x2 + y2)[-1]
v1 = str(x1 + y1)[-1]

digit = int(v1 + v2 + v3)

print(digit)