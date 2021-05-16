s = input()
r = ''
while len(s) != 0:
    r += s[-1]
    s = s[0:-1]

print(r)