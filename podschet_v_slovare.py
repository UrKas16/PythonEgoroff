n = input().lower()

a = {}

for i in n:
    if i.isalpha():
        a[i] = a.get(i, 0) + 1
print(a)

