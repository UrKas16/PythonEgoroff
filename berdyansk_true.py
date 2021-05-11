n = int(input())

slovar = {}

for i in range(n):
    login = input()
    if login in slovar:
        print(f'{login}{slovar[login]}')
        slovar[login] += 1
    else:
        print('OK')
        slovar[login] = 1