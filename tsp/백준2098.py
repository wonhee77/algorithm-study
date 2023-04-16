import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * (1 << n) for _ in range(n)]


def dfs(x, visited):
    if visited == 1:
        if arr[0][x]:
            return arr[0][x]
        else:
            return float('inf')

    if dp[x][visited] != 0:
        return dp[x][visited]

    minimum = float('inf')
    for i in range(1, n):
        if not arr[i][x]:
            continue
        if visited & (1 << i):
            minimum = min(minimum, dfs(i, visited - (1 << i)) + arr[i][x])

    dp[x][visited] = minimum
    return minimum


print(dfs(0, ((1 << n) - 1)))

'''
TSP(Traveling Salesman Problem)

1. Brute force algorithm
 - 모든 순열을 조합으로 최소값 계산
 - from itertools import permutations
    data = ['A', 'B', 'C']
    result = list(permutations(data, 3))
 - n이 조금만 늘어나도 경우의 숫자가 매우 많이 늘어나 비효율적

2. Dynamic programming
 - 지나온 도시들의 최솟값을 기록해놓으면 그 다음 도시로 갈 때의 최솟값은 (현재까지의 최솟값 + 현재 ~ 다음 도시의 거리)를 비교하여 다음 도시로 가는 최솟값을 구할 수 있다.
 - minimum = min(minimum, dfs(i, visited - (1 << i)) + arr[i][x])
 - 방문한 경로도 중요하기 때문에 dp에 visited를 추가하여 어떠한 도시들을 지나 현재 도시로 왔을 때의 최솟값인지 기록한다.
 - dp = [[0] * (1 << n) for _ in range(n)]
 - 비트마스킹을 이용하면 n개의 방문도시를 기록할 때 (1 << n) - 1 로 모든걸 표현할 수 있다. 메모리 절약
 
'''
