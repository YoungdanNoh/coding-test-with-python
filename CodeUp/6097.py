h, w = map(int, input().split())
N = int(input())

cb = []
for i in range(h):
    cb.append([])
    for j in range(w):
        cb[i].append(0)

for n in range(N):
    l, d, x, y = map(int, input().split())

    for L in range(l):
        if d == 0:
            cb[x-1][y-1+L] = 1
        else:
            cb[x - 1 + L][y - 1] = 1

for c in range(h):
    print(*cb[c])