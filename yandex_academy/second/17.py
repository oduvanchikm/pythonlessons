

a = int(input())
b = int(input())
c = int(input())

D = b ** 2 - 4 * a * c

x1 = (b * (-1) - D ** 0.5) / 2 * a
x1 = (b * (-1) + D ** 0.5) / 2 * a

if a == 0 and b == 0 and c == 0:
    print('Infinite solutions')
else:

    if D > 0:
        print(x1, x2)
    elif D == 0:
        print(x1)
    else:
        print('No solution')