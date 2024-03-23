n = int(input())
k = list(map(int, input().split()))

dp = [0]*100
dp[0] = k[0]
dp[1] = k[1]

for i in range(2, n):
    dp[i] = max(dp[i-1], (k[i] + dp[i-2]))

print(dp[n-1])