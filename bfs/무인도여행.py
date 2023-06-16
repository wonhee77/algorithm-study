from collections import deque

def solution(maps):
    h_size = len(maps[0])
    v_size = len(maps)
    visited = [[False] * h_size for _ in range(v_size)]

    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(v_size):
        for j in range(h_size):
            if not visited[i][j] and maps[i][j] != 'X':
                food = 0
                queue = deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    food += int(maps[x][y])
                    for k in range(4):
                        X, Y = x + dx[k], y + dy[k]
                        if 0 <= X < v_size and 0 <= Y < h_size and not visited[X][Y] and maps[X][Y] != 'X':
                            queue.append((X, Y))
                answer.append(food)
    answer.sort()

    return answer if answer else [-1]

