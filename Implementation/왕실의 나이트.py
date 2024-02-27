start = input() #시작 위치
x = int(ord(start[0])) - int(ord('a'))
y = int(start[1]) - 1

move = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

result = 0
for m in move:
    x_ = x + m[0]
    y_ = y + m[1]

    if x_ >= 0 and x_ <= 7 and y_ >= 0 and y_ <= 7:
        result += 1

print(result)