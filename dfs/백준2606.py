import sys

computer_cnt = int(sys.stdin.readline())
connect_cnt = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(connect_cnt)]

visited = [False] * (computer_cnt + 1)

graph = [[] for i in range(computer_cnt + 1)]
for a in arr:
    graph[a[0]].append(a[1])
    graph[a[1]].append(a[0])

def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

dfs(1)

print(visited.count(True) - 1)

"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""