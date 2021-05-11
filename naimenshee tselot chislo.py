n = input()

count = 0

total = 0

for i in range(len(n)):
    if '0' < n[i] < '9':
        count += 1
        total += int(n[i])
print(count, total)