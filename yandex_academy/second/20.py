str1 = input()
str2 = input()
str3 = input()
x = []


if 'зайка' in str1:
    x.append(str1)
if 'зайка' in str2:
    x.append(str2)
if 'зайка' in str3:
    x.append(str3)

x1 = x.slpit()

result = ' '.join(x1) 

print(x1)
print(result)


