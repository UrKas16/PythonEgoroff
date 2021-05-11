n = int(input())

a = []
flag = False

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i > j or i < j and a[i][j] == a[j][i]:
                flag = True
        elif i == j:
            continue
        else:
            print('No')
            flag = False
    break

if flag:
    print('Yes')
