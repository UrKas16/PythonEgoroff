n = input()

stack = []

is_good = True

for i in n:
    if i in '({[':
        stack.append(i)
    elif i in ')}]':
        if not stack:
            is_good = False
            break
        open_break = stack.pop()
        if open_break == '(' and i == ')':
            continue
        if open_break == '{' and i == '}':
            continue
        if open_break == '[' and i == ']':
            continue
        is_good = False
        break
if is_good and len(stack) == 0:
    print('YES')
else:
    print('NO')
