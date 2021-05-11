n, m = map(int, input().split())

pole = []

pole.append('.' * (m + 2))

for i in range(n):
    pole.append('.' + input() + '.')

pole.append('.' * (m + 2))

count = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if pole[i][j] == '.' and not '*' in (pole[i][j - 1], pole[i][j + 1], pole[i - 1][j], pole[i + 1][j]):
            count += 1

print(count)
