
def format_namelist(x):
    a = []
    for i in range(len(x)):
        a.append(x[i]['name'])
    c = ''
    while len(a) > 0:
        for i in a:
            if len(a) > 2:
                c += i + ', '
                a.remove(i)
            elif len(a) == 2:
                c += i
                a.remove(i)
            elif len(a) == 1:
                c += i
                a.remove(i)
            else:
                c += ' и ' + i
                a.remove(i)
    return c


print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]))




