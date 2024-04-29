n = int(input())
arr = map(int, input().split())

arr_s = sorted(arr)

if arr_s[0] > n:
    print(0)
    exit()

cnt = 0
for i in arr_s:
    if i <= len(arr_s):
        for j in range(i):
            arr_s.pop(0)
        cnt += 1

print(cnt)