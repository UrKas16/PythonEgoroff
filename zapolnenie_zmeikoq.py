n, m = map(int, input().split())

for i in range(n):
    x = list(range(i * m, (i + 1) * m))
    if i % 2 == 0:
        print(*x)
    else:
        print(*x[::-1])
