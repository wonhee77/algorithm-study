import sys
from collections import deque

sys.setrecursionlimit(100000)

V, E = map(int, input().split())
S = int(input())

arr = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    arr[u].append((v, w))

dp = [float('inf')] * (V + 1)
dp[S] = 0


def bfs(num):
    queue = deque([num])
    while queue:
        n = queue.popleft()
        tuples = arr[n]
        for target, distance in tuples:
            if dp[n] + distance < dp[target]:
                dp[target] = dp[n] + distance
                queue.append(target)
bfs(S)

for i in range(1, V + 1):
    print(dp[i] if dp[i] != float('inf') else 'INF')

def dfs(num):
    tuples = arr[num]
    tuples.sort(key=lambda x: x[1])
    for target, d in tuples:
        if dp[target] > dp[num] + d:
            dp[target] = dp[num] + d
            dfs(target)
# dfs(S)
