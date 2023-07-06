import sys
from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    ground = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        ground[y][x] = 1

    answer = 0

    for n in range(N):
        for m in range(M):
            if ground[n][m] == 1 and not visited[n][m]:
                answer += 1
                queue = deque()
                queue.append([m, n])
                while queue:
                    q = queue.popleft()
                    x = q[0]
                    y = q[1]
                    if visited[y][x]:
                        continue
                    visited[y][x] = True
                    for i in range(4):
                        X = x + dx[i]
                        Y = y + dy[i]
                        if 0 <= X < M and 0 <= Y < N and not visited[Y][X] and ground[Y][X] == 1:
                            queue.append([X, Y])

    print(answer)



