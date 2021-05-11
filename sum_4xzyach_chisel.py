total = 0

for i in range(10):
    for j in range(10):
        for m in range(10):
            for n in range(10):
                a = int(str(i) + str(j) + str(m) + str(n))
                if a > 999:
                    if i+j+m+n == 20:
                        total += a
print(total)

total = 0

for i in range(1000, 10000):
    a = i % 10
    i //= 10
    b = i % 10
    i //= 10
    c = i % 10
    i //= 10
    d = i
    if a+b+c+d == 20:
        a = int(str(d) + str(c) + str(b) + str(a))
        total += a
print(total)