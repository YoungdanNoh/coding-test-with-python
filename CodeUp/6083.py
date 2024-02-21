R, G, B = map(int, input().split(" "))
n = 0

for r in range(R):
    for g in range(G):
        for b in range(B):
            print(r,g,b)
            n += 1
print(n)