def check_password(args = input()):
    args = str(args)
    count = 0
    znaki = False
    isupper = False
    for i in args:
        if i.isdigit():
            count += 1
        elif i in '!@#$%*':
            znaki = True
        elif i.isupper():
            isupper = True

    if len(args) >= 10 and count >= 3 and znaki and isupper:
        print('Perfect password')
    else:
        print('Easy peasy')

check_password()





