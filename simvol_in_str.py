def count_letters(fraza):
    count_str = 0
    count_upp = 0
    for i in fraza:
        if i.islower():
            count_str += 1
        elif i.isupper():
            count_upp += 1
    print(f'''Количество заглавных символов: {count_upp}
Количество строчных символов: {count_str}''')


count_letters()
