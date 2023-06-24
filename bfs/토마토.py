import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
plate = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def solution():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if plate[i][j] == 1:
                queue.append((i, j))

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and plate[ny][nx] == 0:
                plate[ny][nx] = plate[y][x] + 1
                queue.append((ny, nx))

    max_val = 0

    for a in range(N):
        for b in range(M):
            if plate[a][b] == 0:
                return -1
            max_val = max(max_val, plate[a][b])
    return max_val - 1


print(solution())