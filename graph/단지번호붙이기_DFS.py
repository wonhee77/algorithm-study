import sys

N = int(sys.stdin.readline())
graph = []
visited = [[False] * N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    graph.append(list(map(int, list(sys.stdin.readline())[:-1])))

answer = []

cnt = 0
def dfs(x, y):
    if graph[x][y] == 0 | visited[x][y]:
        return

    visited[x][y] = True
    global cnt
    cnt += 1
    for i in range(4):
        if (0 <= x + dx[i] < N) & (0 <= y + dy[i] < N):
            dfs(x + dx[i], y + dy[i])


for i in range(N):
    for j in range(N):
        dfs(i, j)
        if cnt != 0:
            answer.append(cnt)
            cnt = 0

print(len(answer))
answer.sort()
for num in answer:
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