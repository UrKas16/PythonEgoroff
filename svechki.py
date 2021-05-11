a, b = map(int, input().split())

count = 0

while a != 0:
    count += a
    a = a // b
print(int(count))