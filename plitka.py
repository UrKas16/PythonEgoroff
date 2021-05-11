n = 4

a = []

for i in range(n):
    a.append(''.join(input()))

for i in a:
    print(i)

flag = True

for i in range(n - 1):
    for j in range(n - 1):
        if a[i][j] == a[i][j + 1] == a[i + 1][j] == a[i + 1][j + 1]:
            flag = False
if flag:
    print('Yes')
else:
    print('No')
