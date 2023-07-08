import sys

N = int(input())
prices = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[] for _ in range(N)]
dp[0] = (prices[0])

for i in range(1, N):
    dp[i].append(min(dp[i - 1][1] + prices[i][0], dp[i - 1][2] + prices[i][0]))
    dp[i].append(min(dp[i - 1][0] + prices[i][1], dp[i - 1][2] + prices[i][1]))
    dp[i].append(min(dp[i - 1][0] + prices[i][2], dp[i - 1][1] + prices[i][2]))

print(min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))
