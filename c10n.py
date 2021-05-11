n = int(input())

a = ''

for i in range(n):
    s = input()
    if len(s) > 10:
        a += s[1:-1]
        print(s[0] + str(len(a)) + s[-1])
    else:
        print(s)
    a = ''