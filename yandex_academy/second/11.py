digit = int(input())

digit_1 = str(digit)

d1 = int(digit_1[0])
d2 = int(digit_1[1])
d3 = int(digit_1[2])

d_max = max(d1, d2, d3)
d_min = min(d1, d2, d3)

d_sum = d_max + d_min

middle = (d1 + d2 + d3) - d_sum

a = middle * 2

if d_sum == a:
    print('YES')
else:
    print('NO')
