import heapq

def solution(n, s, a, b, fares):
    def dijkstra(start):
        distance = [float('INF') for _ in range(n + 1)]
        distance[start] = 0
        q = []
        heapq.heappush(q, (distance[start], start))

        while q:
            fare_now, current_des = heapq.heappop(q)
            for next_des, fare_next in graph[current_des]:
                if distance[next_des] > fare_now + fare_next:
                    distance[next_des] = fare_now + fare_next
                    heapq.heappush(q, ([distance[next_des], next_des]))
        return distance

    ans = 200000001
    graph = [[] for _ in range(n + 1)]
    for i, j, c in fares:
        graph[i].append((j, c))
        graph[j].append((i, c))

    dist = [[]]
    for i in range(1, n + 1):
        dist.append(dijkstra(i))

    for i in range(1, n + 1):
        ans = min(ans, dist[s][i] + dist[i][a] + dist[i][b])
    return ans


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24],
                [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))