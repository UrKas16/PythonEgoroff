n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(input())

mas = [[False] * m for i in range(n)]

for i in range(n):
    if 'S' not in a[i]:
        for j in range(m):
            mas[i][j] = True

for j in range(m):
    is_find = False
    for i in range(n):
        if a[i][j] == 'S':
            is_find = True
            break
    if not is_find:
        for i in range(n):
            mas[i][j] = True

count = 0

for i in mas:
    count += i.count(True)
print(count)





