import sys

T = int(sys.stdin.readline())
house = []
max_floor = 0
for _ in range(T):
    k = int(sys.stdin.readline())
    max_floor = max(max_floor, k)
    n = int(sys.stdin.readline())
    house.append([k, n])

dp = [[0] * 21 for _ in range(max_floor + 1)]

for i in range(max_floor + 1):
    for j in range(1, 21):
        if i == 0:
            dp[0][j] = j
        else:
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

for i in range(T):
    print(dp[house[i][0]][house[i][1]])
