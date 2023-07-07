import sys
from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)

queue = deque([1])
visited[1] = True

while queue:
    num = queue.popleft()
    nums = graph[num]
    for n in nums:
        if not visited[n]:
            visited[n] = True
            parent[n] = num
            queue.append(n)

for k in range(2, N + 1):
    print(parent[k])

