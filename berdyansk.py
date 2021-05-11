n = int(input())

slovar = {}

for i in range(n):
    login = input()
    if login not in slovar:
        slovar.setdefault(login, login)
        print('OK')
    else:
        slovar1 = {}
        count = 0
        for i, j in slovar.items():
            if j == login:
                count += 1
        slovar.setdefault(login + str(count), login)
        slovar1.setdefault(login + str(count), login)
        for key in slovar1:
            print(key)

