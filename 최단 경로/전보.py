import heapq

n, m, c = map(int, input().split())
INF = int(1e9)

graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        time, dest = heapq.heappop(q)

        if distance[dest] < time:
            continue
        for i in graph[dest]:
            cost = time + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(c)

city = 0
max_t = 0

for i in range(1, n+1):
    if distance[i] != INF and i != c:
        city += 1
        max_t = max(max_t, distance[i])

if city != 0:
    print(city, end=" ")
    print(max_t)
else:
    print("Not found")