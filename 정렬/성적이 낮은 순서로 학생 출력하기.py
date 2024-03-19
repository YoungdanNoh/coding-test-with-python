n = int(input())
name = []
score = []

for i in range(n):
    temp = input().split()
    name.append(temp[0])
    score.append(temp[1])

for i in range(len(score)):
    min_idx = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(score)):
        if score[min_idx] > score[j]:
            min_idx = j
    score[i], score[min_idx] = score[min_idx], score[i]
    name[i], name[min_idx] = name[min_idx], name[i]

print(*name)