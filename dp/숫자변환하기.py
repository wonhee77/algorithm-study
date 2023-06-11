def solution(x, y, n):
    dp = [float('inf')] * (y + 1)
    dp[x] = 0

    for i in range(x, y + 1):
        if dp[i] == float('inf'):
            continue
        cnt = dp[i]
        a = i + n
        b = i * 2
        c = i * 3
        if a <= y:
            dp[a] = min(dp[a], cnt + 1)
        if b <= y:
            dp[b] = min(dp[b], cnt + 1)
        if c <= y:
            dp[c] = min(dp[c], cnt + 1)

    return dp[y] if dp[y] != float('inf') else -1


'''
가장 쉽게 생각하면 3가지 경우를 모두 계산하며 y값에 도달했을 때의 최소값을 구하면 된다.
하지만 각각의 경우가 겹치는 경우가 있기 때문에 모두 계산을 하면 시간 측면에서 효율적이지 못하다.
dp를 사용해 특정 값에 도달하는 최소값을 구해놓으면 그 값에서 이전 결과를 알 필요 없이 다시 최소를 구하면 된다.
모든 경우를 다 계산해야 답이 나올것 같은 상황에서는 dp를 생각해보자.
'''