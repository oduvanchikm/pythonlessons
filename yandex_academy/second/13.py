elves = int(input())
dwarves = int(input())
humans = int(input())


e1 = elves // 10
e2 = elves % 10

d1 = dwarves // 10
d2 = dwarves % 10

h1 = humans // 10
h2 = humans % 10

if e1 == d1 == h1:
    print(e1)
if e2 == d2 == h2:
    print(e2)