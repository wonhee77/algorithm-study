import sys
from collections import deque

N = int(sys.stdin.readline())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = []

for _ in range(N):
    graph.append(list(map(int, list(sys.stdin.readline())[:-1])))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 0
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 1:
            graph[x][y] = 0
            cnt += 1
            for i in range(4):
                if (0 <= x + dx[i] < N) & (0 <= y + dy[i] < N):
                    queue.append((x + dx[i], y + dy[i]))
    return cnt


for i in range(N):
    for j in range(N):
        cnt = bfs(i, j)
        if cnt != 0:
            answer.append(cnt)

print(len(answer))
for num in sorted(answer):
    print(num)

"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
