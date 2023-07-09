N = int(input())
M = int(input())
S = input()
dp = [0] * M
if S[0] == 'I':
    dp[0] = 1

answer = 0

for i in range(1, M):
    if S[i] == 'I':
        if S[i - 1] == 'O' and dp[i - 1] != 0:
            dp[i] = dp[i - 1] + 1
            if dp[i] >= (N * 2 + 1):
                answer += 1
        else:
            dp[i] = 1
    else:
        if S[i - 1] == 'I':
            dp[i] = dp[i - 1] + 1

print(answer)