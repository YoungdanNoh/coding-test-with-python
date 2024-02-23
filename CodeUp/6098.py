cb = []

for i in range(10):
    cb.append(list(map(int, input().split())))

x, y = 1, 1 # 처음 위치
cb[x][y] = 9
flag = True

while flag:
    if x == 9 and y == 9: # 맨 아래 가장 오른쪽이라면
        flag = False
    else:
        if cb[x][y+1] == 0: #오른쪽 길이 갈 수 있다면
            cb[x][y+1] = 9
            y += 1
            
        elif cb[x+1][y] == 0: #오른쪽으로 가지 못하고 아래쪽으로 갈 수 있다면
            cb[x+1][y] = 9
            x += 1
            
        else: #더 이상 이동이 불가능하다면
            if cb[x][y+1] == 2: #먹이의 위치라면
                cb[x][y+1] = 9
            elif cb[x+1][y] == 2: #먹이의 위치라면
                cb[x+1][y] = 9
            flag = False

for c in range(10):
    print(*cb[c])