n = int(input())
s = list(map(int, input().split()))
b = []

for j in range(len(s) - 1):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            b.pop()
            b.append(s[i + 1])
            while b[0] < s[i]:
                s[i], s[i + 1] = s[i + 1], s[i]
                i -= 1
print(*s)
