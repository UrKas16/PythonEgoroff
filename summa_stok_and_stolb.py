n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    count_m = 0
    for j in range(m):
        count_m += a[i][j]
    print(count_m, end=' ')

print()

for j in range(m):
    count_n = 0
    for i in range(n):
        count_n += a[i][j]
    print(count_n, end=' ')