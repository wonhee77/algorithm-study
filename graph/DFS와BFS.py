import sys
from collections import deque

N, M, V = map(int, input().split())

nodes = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited = [False] * (N + 1)
dfs_answer = []
def dfs(num):
    visited[num] = True
    dfs_answer.append(num)
    arr = nodes[num]
    arr.sort()
    for i in range(len(arr)):
        if not visited[arr[i]]:
            dfs(arr[i])

dfs(V)
print(' '.join(map(str, dfs_answer)))

queue = deque()
queue.append(V)
visited = [False] * (N + 1)
bfs_answer = []
while queue:
    n = queue.popleft()
    if visited[n]:
        continue
    bfs_answer.append(str(n))
    visited[n] = True
    node = nodes[n]
    node.sort()
    for a in node:
        if not visited[a]:
            queue.append(a)

print(' '.join(bfs_answer))


