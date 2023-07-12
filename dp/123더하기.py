import sys

T = int(input())
nums = []
for _ in range(T):
    nums.append(int(sys.stdin.readline().rstrip()))

max_int = max(nums)

dp = [0] * (max_int + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_int + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for n in nums:
    print(dp[n])
