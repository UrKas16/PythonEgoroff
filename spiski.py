n, m = map(int, input().split())

sp_1 = list(map(int, input().split()))
sp_2 = list(map(int, input().split()))

sp_3 = sp_1 + sp_2

sp_4 = []

while len(sp_4) != len(sp_3):
    if len(sp_2) == 0:
        sp_4.insert(0, sp_1[-1])
        sp_1.remove(sp_4[0])
    elif len(sp_1) == 0:
        sp_4.insert(0, sp_2[-1])
        sp_2.remove(sp_4[0])
    elif sp_1[-1] >= sp_2[-1]:
        sp_4.insert(0, sp_1[-1])
        sp_1.remove(sp_4[0])
    else:
        sp_4.insert(0, sp_2[-1])
        sp_2.remove(sp_4[0])
print(*sp_4)