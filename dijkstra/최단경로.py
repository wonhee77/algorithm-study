import heapq
import sys

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def dijkstra(start):
    distance = [float('inf')] * (V + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dis, node = heapq.heappop(queue)
        if distance[node] < dis:
            continue
        tuples = graph[node]
        for n, d in tuples:
            if distance[n] > distance[node] + d:
                distance[n] = distance[node] + d
                heapq.heappush(queue, (distance[n], n))
    return distance

d = dijkstra(K)
for i in range(1, V + 1):
    print(d[i] if d[i] != float('inf') else 'INF')