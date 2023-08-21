digit = int(input())

digit_1 = str(digit)

d1 = int(digit_1[0])
d2 = int(digit_1[1])
d3 = int(digit_1[2])

sum_1 = d2 + d3
sum_2 = d1 + d2

if sum_1 > sum_2:
    print(f'{sum_1}{sum_2}')
else:
    print(f'{sum_2}{sum_1}')
