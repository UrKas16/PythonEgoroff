n = input()

a = list(set(n))

b = [0] * len(n)

for i in range(len(a)):
    c = n.index(a[i])
    b.insert(c, n[c])
    b.pop(c + 1)

while 0 in b:
    b.remove(0)

print(''.join(b))




