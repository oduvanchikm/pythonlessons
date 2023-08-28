digit1 = int(input())
digit2 = int(input())

a = digit1 // 10
b = digit1 % 10

c = digit2 // 10
d = digit2 % 10

mmin = min(a, b, c, d)
mmax = max(a, b, c, d)

summ_b_c = str((a + b + c + d) - (mmin + mmax))[-1]

print(f'{mmax}{summ_b_c}{mmin}')