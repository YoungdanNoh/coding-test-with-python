N, M = map(int, input().split())
x, y, d = map(int, input().split()) #좌표, 방향

m = []
visit = [] #방문 정보 저장
for _ in range(N):
    m.append(list(map(int, input().split())))
    visit.append([0 for i in range(M)])

# 북, 동, 남, 서
direc = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def left():
    global d
    d -= 1 # 왼쪽으로 회전하면 direc 리스트에서도 해당되는 인덱스를 찾아 방향 설정을 하기 위함
    if d == -1:
        d = 3 # 0 -> 3, 2, 1, 0

cnt = 0 #방문 칸 수
turn = 0 #회전 수
while True:
    left() #회전
    x_ = x + direc[d][0]
    y_ = y + direc[d][1]

    if m[x_][y_] == 0 and visit[x_][y_] == 0: #이동가능
        visit[x_][y_] = 1
        x = x_
        y = y_
        cnt += 1
        turn = 0
        continue
    else: #이동 불가
        turn += 1
    if turn == 4: # 전 방향 이동이 불가능하다면
        x_ = x - direc[d][0]
        y_ = y - direc[d][1]
        if m[x_][y_] == 0: #뒤로 이동이 가능할 때는 이동한다
            x = x_
            y = y_
        else: #뒤가 바다라면 움직임을 멈춘다
            break
        turn = 0
print(cnt)