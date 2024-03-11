N, M = map(int, input().split(' '))

ice = []
for i in range(N):
    ice.append(list(map(int, input())))

def dfs(x, y):
    # 범위를 벗어났다면
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    if ice[x][y] == 0: #방문하지 않은 곳이라면
        # 방문처리
        ice[x][y] = 1

        dfs(x-1, y) #위로
        dfs(x+1, y) #아래로
        dfs(x, y-1) #좌로
        dfs(x, y+1) #우로
        return True
    return False

result = 0
for j in range(N):
    for k in range(M):
        if dfs(j, k) == True:
            result += 1
print(result)