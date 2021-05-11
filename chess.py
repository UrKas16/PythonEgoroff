a = input()
b = input()

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

a1 = list.index(a[0]) + 1
a2 = int(a[1])
b1 = list.index(b[0]) + 1
b2 = int(b[1])

c = [a1, a2, b1, b2]

if sum(c) % 2 == 0:
    print('YES')
else:
    print('NO')