import sys
sys.setrecursionlimit(100000)

N = int(input())
graph = [sys.stdin.readline().rstrip() for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs1(spot):
    x, y = spot[0], spot[1]
    visited[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
            dfs1([nx, ny])

answer1 = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            answer1 += 1
            dfs1([i, j])

answer2 = 0
visited = [[False] * N for _ in range(N)]
for l in range(N):
    graph[l] = graph[l].replace('R', 'G')

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            answer2 += 1
            dfs1([i, j])

print(answer1, answer2)