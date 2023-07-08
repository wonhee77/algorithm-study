import heapq
import sys

N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, v = map(int, sys.stdin.readline().split())
    graph[s].append((v, e))

answer = 0

def dijkstra(start):
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current, city = heapq.heappop(queue)
        if distance[city] < current:
            continue

        for v, e in graph[city]:
            if distance[e] > v + current:
                distance[e] = v + current
                heapq.heappush(queue, (distance[e], e))
    return distance

for i in range(1, N + 1):
    go = dijkstra(i)[X]
    back = dijkstra(X)[i]
    answer = max(answer, go + back)

print(answer)