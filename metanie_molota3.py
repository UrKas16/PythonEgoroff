n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(list(map(int, input().split())))
c = []

for i in range(n):
    c.append(max(a[i]))

print(c.count(max(c)))
