import sys
from collections import deque

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break
    m = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    answer = 0

    for y in range(h):
        for x in range(w):
            if m[y][x] == 1 and not visited[y][x]:
                answer += 1
                queue = deque([(y, x)])
                while queue:
                    Y, X = queue.popleft()
                    if visited[Y][X]:
                        continue
                    visited[Y][X] = True
                    for i in range(8):
                        new_Y = Y + dy[i]
                        new_X = X + dx[i]
                        if 0 <= new_Y < h and 0 <= new_X < w and m[new_Y][new_X] == 1:
                            queue.append((new_Y, new_X))
    print(answer)


