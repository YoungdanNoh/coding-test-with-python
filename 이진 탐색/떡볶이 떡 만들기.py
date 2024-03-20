n, m = map(int, input().split()) # 떡의 개수, 요청한 떡의 길이
h = list(map(int, input().split())) # 떡의 개별 높이

'''
절단기의 높이는 0부터 10억까지의 정수 중 하나이다.
이렇게 큰 탐색 범위를 보면 가장 먼저 이진 탐색을 떠올려야 한다.
이와 같이 큰 범위일 때 단순히 선형탐색을 수행하면 시간초과가 날 수 있기 때문이다.
'''
'''
sum = 0
for i in range(max(h), -1, -1):
    for j in range(n):
        if (h[j] - i) >= 0:
            sum = sum + (h[j] - i)
    if sum >= m:
        print(i)
        break
    else:
        sum = 0
'''

start = 0
end = max(h)

while start <= end:
    tot = 0
    mid = (start + end) // 2
    for x in h:
        if x > mid:
            tot += x - mid
    if tot < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)