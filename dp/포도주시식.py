import sys

n = int(sys.stdin.readline())
wine = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0] * n

max_num = 0

for i in range(n):
    if i == 0:
        dp[0] = wine[0]
        continue
    if i == 1:
        dp[1] = wine[0] + wine[1]
        continue
    if i == 2:
        dp[2] = max(wine[0] + wine[1], wine[0] + wine[2], wine[1] + wine[2])
        continue

    dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i], dp[i - 1])
    if dp[i] > max_num:
        max_num = dp[i]
print(dp[n - 1])
