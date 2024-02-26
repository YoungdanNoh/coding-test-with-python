N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
flag = True
tot = 0

for i in range(M):
    if flag:
        tot += arr[0]
        if (i+1) % K == 0:
            flag = False
    else:
        tot += arr[1]
        flag = True

print(tot)