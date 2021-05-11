n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(list(map(int, input().split())))
c = [0]

for i in range(n):
    for j in range(m):
        if a[i][j] > c[0]:
            c.insert(0, a[i][j])
            c.pop()
            ind_i = i
            ind_j = j

print(c[0])
print(ind_i, ind_j)
