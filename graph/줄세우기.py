import sys
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    indegree[y] += 1

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
answer = []

while queue:
    num = queue.popleft()
    answer.append(num)
    arr = graph[num]
    for a in arr:
        indegree[a] -= 1
        if indegree[a] == 0:
            queue.append(a)

print(' '.join(map(str, answer)))


