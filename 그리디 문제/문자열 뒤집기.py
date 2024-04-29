s = list(map(int, input()))

cnt = []
for iv in range(2):
    tmp = 0
    flag = False
    for i in range(len(s)):
        if s[i] != iv and not flag:
            tmp += 1
            flag = True
        elif s[i] == iv:
            flag = False
    cnt.append(tmp)
print(min(cnt))