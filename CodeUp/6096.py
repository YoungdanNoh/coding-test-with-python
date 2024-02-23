cb = []

for i in range(19):
    cb.append(list(map(int, input().split())))

n = int(input())

for j in range(n):
    x, y = map(int, input().split())
    for c in range(19):
        if cb[c][y-1] == 0:
            cb[c][y-1] = 1
        else:
            cb[c][y-1] = 0

        if cb[x-1][c] == 0:
            cb[x-1][c] = 1
        else:
            cb[x-1][c] = 0

for k in range(19):
    print(*cb[k])