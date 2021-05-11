boys = int(input())
lvl_b = sorted(list(map(int, input().split())))[:boys]

girls = int(input())
lvl_g = sorted(list(map(int, input().split())))[:girls]

count = 0

s = min(boys, girls)

while s:
    if lvl_b[0] == lvl_g[0] or lvl_b[0] == lvl_g[0] + 1 or lvl_b[0] == lvl_g[0] - 1:
        count += 1
        lvl_b = lvl_b[1:]
        lvl_g = lvl_g[1:]
        s -= 1
    elif lvl_b[0] != lvl_g[0] or lvl_b[0] != lvl_g[0] + 1 or lvl_b[0] != lvl_g[0] - 1:
        lvl_b = lvl_b[1:]
        lvl_g = lvl_g[1:]
        s -= 1
print(count)
