def solution(land):
    dp = [[0] * 4 for _ in range(len(land))]
    dp[0] = land[0]

    for i in range(1, len(land)):
        for j in range(4):
            max_val = 0
            for k in range(4):
                if k != j:
                    max_val = max(max_val, dp[i - 1][k])
            dp[i][j] = max_val + land[i][j]

    return max(dp[-1])