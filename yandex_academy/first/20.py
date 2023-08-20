n = int(input())
m = int(input())
k_1 = int(input())
k_2 = int(input())

x = int((n * m - k_2 * n) / (k_1 - k_2))
y = int(n - x)

print(x, y)