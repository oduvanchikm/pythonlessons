digit = int(input())

d1 = digit // 100
d2 = (digit // 10) % 10
d3 = digit % 10

maximum = max(d1, d2, d3)
minimum = min(d1, d2, d3)
middle = (d1 + d2 + d3) - (maximum + minimum)

if minimum == 0:
    print(f'{middle}{minimum} {maximum}{middle}')
else:
    print(f'{minimum}{middle} {maximum}{middle}')