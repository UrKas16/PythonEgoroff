n = list(map(int, ''.join(input())))

s = [0] * 10

for i in n:
    s[i] += 1
for i in range(len(s)):
    if s[i] > 0:
        print(i, s[i])
