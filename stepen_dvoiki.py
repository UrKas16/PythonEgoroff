n = int(input())

count = 0
while n % 2 == 0:
    n /= 2
    count += 1
if n in (1, 2):
    print(count)
else:
    print('НЕТ')
