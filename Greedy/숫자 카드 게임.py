N, M = map(int, input().split())
card = []

for _ in range(N):
    card.append(list(map(int, input().split())))

m = []
for i in range(N):
    m.append(min(card[i]))
print(max(m))