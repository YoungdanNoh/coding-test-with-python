n = int(input())
num = list(map(int, input().split()))

answer = []

for i in range(23):
    answer.append(0)

for j in num:
    answer[j-1] = answer[j-1] + 1

print(*answer)