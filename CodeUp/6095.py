cb = []

for i in range(19):
    cb.append([])
    for j in range(19):
        cb[i].append(0)

n = int(input())

for k in range(n):
    x, y = map(int, input().split())
    cb[x-1][y-1] = 1

for c in range(19):
    print(*cb[c])