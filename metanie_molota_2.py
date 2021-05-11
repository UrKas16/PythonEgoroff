n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(list(map(int, input().split())))
c = [0]
d = []
e = []

for i in range(n):
    for j in range(m):
        if a[i][j] >= c[0]:
            c.insert(0, a[i][j])
            ind_i = i
            if c[0] != c[1]:
                c.pop()
for i in range(n):
    total = 0
    for j in range(m):
        if c[0] in a[i]:
            total += a[i][j]
    d.append(total)
    e.append(i)

if len(c) == 1:
    print(ind_i)
elif d.count(max(d)) > 1:
    print(0)
else:
    print(e[d.index(max(d))])
