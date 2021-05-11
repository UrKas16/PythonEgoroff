n = list(map(int, input().split()))

while len(n):
    for i in range(n[0]):
        print('*', end='')
    n.pop(0)
    print()
