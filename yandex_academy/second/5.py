n = int(input())
m = int(input())

P = 7
V = 6

V1 = V + 6 + m
P1 = P - 1 + n

if V1 > P1:
    print('Вася')
else:
    print('Петя')