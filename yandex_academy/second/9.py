name1 = input()
name2 = input()
name3 = input()

n1 = str(name1[0])
n2 = str(name2[0])
n3 = str(name3[0])


if n1 < n2 and n1 < n3:
    print(name1)
if n2 < n1 and n2 < n3:
    print(name2)
if n3 < n1 and n3 < n2:
    print(name3)


