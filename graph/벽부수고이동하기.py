import sys
from collections import deque

H, W = map(int, input().split())
graph = [sys.stdin.readline() for _ in range(H)]

answer = float('inf')
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[[False, False] for _ in range(W)] for _ in range(H)]

def bfs(h, w):
    queue = deque([(h, w, 1, True)])
    while queue:
        y, x, cnt, chance = queue.popleft()
        if y == H - 1 and x == W - 1:
            global answer
            answer = cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < W and 0 <= ny < H:
                if graph[ny][nx] == '0' and not visited[ny][nx][0]:
                    visited[ny][nx][0] = True
                    queue.append((ny, nx, cnt + 1, chance))
                if graph[ny][nx] == '1' and chance:
                    visited[ny][nx][1] = True
                    queue.append((ny, nx, cnt + 1, False))

visited[0][0][0] = True
bfs(0, 0)

print(answer if answer != float('inf') else -1)
