n = int(input())

a = []

for i in range(n):
    a.append(list(map(int, input().split())))

count = 0

b = []

for i in range(n):
    for j in range(2):
        if j == 1:
            b.append(a[i][j])

for i in range(n):
    for j in range(2):
        if j == 0:
            count += b.count(a[i][j])

print(count)