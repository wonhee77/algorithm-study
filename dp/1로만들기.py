from collections import deque

N = int(input())
dp = [float('inf')] * (N + 1)

queue = deque([1])
dp[1] = 0

while queue:
    num = queue.popleft()
    if num >= N:
        break
    for i in [num * 2, num * 3, num + 1]:
        if i <= N and dp[i] > dp[num] + 1:
            dp[i] = dp[num] + 1
            queue.append(i)

print(dp[N])