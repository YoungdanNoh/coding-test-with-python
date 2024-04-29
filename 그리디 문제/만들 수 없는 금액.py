n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

i = 1
while True:
    tmp = i
    for j in range(n):
        if tmp >= arr[j]:
            tmp = tmp - arr[j]
        if tmp == 0:
            break

    if tmp != 0:
        print(i)
        break
    i += 1