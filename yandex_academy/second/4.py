P = int(input())
V = int(input())
T = int(input())

if P > V and P > T:
    print('1. Петя')
    if V > T:
        print('2. Вася')
        print('3. Толя')
    else:
        print('2. Толя')
        print('3. Вася')
if V > P and V > T:
    print('1. Вася')
    if P > T:
        print('2. Петя')
        print('3. Толя')
    else:
        print('2. Толя')
        print('3. Петя')
if T > P and T > V:
    print('1. Толя')
    if P > V:
        print('2. Петя')
        print('3. Вася')
    else:
        print('2. Вася')
        print('3. Петя')