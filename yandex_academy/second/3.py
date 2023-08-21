P = int(input())
V = int(input())
T = int(input())

if P > V and P > T:
    print("Петя")
if V > P and V > T:
    print("Вася")
if T > P and T > V:
    print("Толя")