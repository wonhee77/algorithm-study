import sys
from collections import deque

T = int(input())

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

for _ in range(T):
    l = int(sys.stdin.readline().rstrip())
    a, b = map(int, sys.stdin.readline().split())
    c, d = map(int, sys.stdin.readline().split())

    visited = [[False] * l for _ in range(l)]

    queue = deque([(a, b, 0)])
    visited[a][b] = True
    answer = 0
    while queue:
        x, y, cnt = queue.popleft()
        if x == c and y == d:
            answer = cnt
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))

    print(answer)