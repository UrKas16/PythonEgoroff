n = input()
m = input()

a = {}

anno = True

for i in range(len(n)):
    a[i] = n[i]
    if a[i] not in m or len(n) != len(m):
        print('NO')
        anno = False
        break
if anno:
    print('YES')
