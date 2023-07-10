import sys

N, M = map(int, input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

for k in range(3):
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                visited[i][j] = True

