n = int(input())

count = 0

for i in range(n + 1, n * 2):
    if i % 2 == 0 and i != 2 or i == 1:
        continue
    d = 3
    is_plane = True
    while d * d <= i:
        if i % d == 0:
            is_plane = False
            break
        d += 2
    if is_plane:
        count += 1
print(count)