from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        n = queue.popleft()
        print(n, end='')

        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

