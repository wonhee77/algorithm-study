import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

arr = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(num):
    visited[num] = True
    nums = arr[num]
    for n in nums:
        if not visited[n]:
            dfs(n)

answer = 0

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        answer += 1
print(answer)