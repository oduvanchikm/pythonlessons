digit = int(input())

digit1 = str(digit)

d = digit1[::-1]

if digit1 == d:
    print('YES')
else:
    print('NO')