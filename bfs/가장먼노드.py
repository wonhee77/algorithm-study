from collections import deque

def bfs(start, graph, distance):
    distance[start] = 1
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for a in graph[node]:
            if distance[a] == 0:
                distance[a] = distance[node] + 1
                queue.append(a)

def solution(n, edge):
    dp = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    bfs(1, graph, dp)

    max_dist = max(dp)
    return dp.count(max_dist)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

"""
그래프 구조에서 최단거리로 이동했을 때 간선의 숫자가 가장 많은 노드의 개수를 구하는 문제
BFS로 탐색하며 답을 찾아나가되 하나의 노드에 도착하는 방법이 여러개인 경우 최솟값으로 값을 교체하려고 했다.
하지만 해당 문제에서는 노드간의 거리가 모두 같다.
BFS 특성상 특정 노드의 거리가 이미 입력된 경우 그 다음 방문시에는 거리가 크거나 같은 경우 밖에 없기 때문에
이미 값이 있는 경우에는 추가적으로 값을 업데이트할 필요가 없다.
"""