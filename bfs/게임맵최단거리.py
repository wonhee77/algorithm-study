from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False] * m for _ in range(n)]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y, 1))
        visited[0][0] = True
        while queue:
            X, Y, cnt = queue.popleft()
            if X == m - 1 and Y == n - 1:
                return cnt
            for i in range(4):
                new_x, new_y = X + dx[i], Y + dy[i]
                if 0 <= new_x < m and 0 <= new_y < n:
                    if maps[new_y][new_x] == 1 and not visited[new_y][new_x]:
                        queue.append((new_x, new_y, cnt + 1))
                        visited[new_y][new_x] = True
        return -1

    return bfs(0, 0)
