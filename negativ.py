n, m = map(int, input().split())

foto = []

for i in range(n):
    foto.append(input())

input()

negativ = []

for i in range(n):
    negativ.append(input())

count = 0

for i in range(n):
    for j in range(m):
        a = foto[i][j]
        b = negativ[i][j]
        if a == b:
            count += 1

print(count)
