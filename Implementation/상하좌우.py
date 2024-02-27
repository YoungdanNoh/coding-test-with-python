N = int(input())
move = list(input().split())

x, y = 0, 0
# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for m in move:
    if m == "R" and y < (N-1): #오른쪽으로 움직일 수 있다면
        y = y + dy[0]
    elif m == "L" and y > 0: #왼쪽으로 움직일 수 있다면
        y = y + dy[1]
    elif m == "U" and x > 0: #위로 움직일 수 있다면
        x = x + dx[3]
    elif m == "D" and x < (N-1): #아래로 움직일 수 있다면
        x = x + dx[2]

print((x+1), (y+1))