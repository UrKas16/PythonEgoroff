n = input()
a = set()
a.add(n)
c = ['Били', 'Вили', 'Дили']
while n != 'конец':
    n = input()
    if n == 'конец':
        break
    else:
        a.add(n)

a = list(a)

for i in range(len(a)):
    a[i] = a[i].split(':')

b = {}

for i in range(len(a)):
    if a[i][0] not in b:
        b[a[i][0]] = 1
    else:
        b[a[i][0]] += 1

j = 0
for i in range(len(c)):
    if c[j] in b:
        j += 1
    else:
        b[c[j]] = 0

a = sorted(b.items(), key=lambda i: i[1], reverse=True)



for i in range(len(a)):
    print(f'Количество уникальных комментаторов у {a[i][0]} - {a[i][1]}')
