import sys
from collections import deque

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n + 1)
queue = deque([p1])

answer = -1

while queue:
    person = queue.popleft()
    if person == p2:
        answer = visited[p2]
        break
    people = graph[person]
    for p in people:
        if visited[p] == 0:
            visited[p] = visited[person] + 1
            queue.append(p)
print(answer)

