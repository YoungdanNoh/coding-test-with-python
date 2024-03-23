t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    gold = list(map(int, input().split()))

    gold_ = []
    cnt = 0
    for j in range(n):
        gold_.append([])
        for k in range(m):
            gold_[-1].append(gold[cnt])
            cnt += 1

    dp = [0] * (m+1)

    #dx = [-n, 1, 1, m+1]
    dx = [-1, 0, 1]
    dy = [1, 1, 1]
    #오른쪽 위, 오른쪽, 오른쪽 아래

    x = 0
    y = 0
    x_temp = 0
    y_temp = 0
    for d in range(1, m+1):
        if d == 1:
            # 첫번째 시작위치 지정
            dp[d] = gold_[x][y]
            for n_ in range(1, n):
                if dp[d] < gold_[n_][0]:
                    dp[d] = gold_[n_][0]
                    x = n_
        else:
            for d_ in range(len(dx)):
                # 전 방향으로 이동하며 가장 큰 값을 찾는다.
                if (x + dx[d_]) < 0 or (x + dx[d_]) >= n or (y + dy[d_]) < 0 or (y + dy[d_]) >= m:
                    continue
                else:
                    x_ = x + dx[d_]
                    y_ = y + dy[d_]
                    if dp[d] < dp[d-1] + gold_[x_][y_]:
                        dp[d] = dp[d-1] + gold_[x_][y_]
                        x_temp = x_
                        y_temp = y_
            x = x_temp
            y = y_temp
    print(dp[m], end= ' ')