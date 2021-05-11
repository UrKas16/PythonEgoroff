n, x = map(int, input().split())

tabl = []

for i in range(n):
    tabl.append([0] * n)

for i in range(n):
    for j in range(n):
        tabl[i].append((i + 1) * (j + 1))
        tabl[i].pop(0)

count = 0

for i in range(n):
    for j in range(n):
        if tabl[i][j] == x:
            count += 1

print(count)
