n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(input().split())

flag = True

for i in range(n):
    for j in range(m):
        if a[i][j] == 'C' or a[i][j] == 'M' or a[i][j] == 'Y':
            break
        else:
            flag = False

if flag:
    print('#Color')
else:
    print('#Black&White')
