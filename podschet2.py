n = int(input())
m = list(map(int, input().split()))

a = max([abs(min(m)), abs(max(m))]) * 2 + 1

s = [0] * a

for i in m:
    number = i + int(a / 2)
    s[number] += 1

for i in range(len(s)):
    if s[i] > 0:
        print((str(i - int(a / 2)) + ' ') * s[i], end='')
