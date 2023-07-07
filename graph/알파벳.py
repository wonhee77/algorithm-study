H, W = map(int, input().split())
graph = [input() for _ in range(H)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
s = set(graph[0][0])

def dfs(h, w, depth):
    global answer
    answer = max(answer, depth)
    for i in range(4):
        x = w + dx[i]
        y = h + dy[i]
        if 0 <= x < W and 0 <= y < H and graph[y][x] not in s:
            s.add(graph[y][x])
            dfs(y, x, depth + 1)
            s.remove(graph[y][x])

dfs(0, 0, 1)
print(answer)
