import sys

v, e = map(int, sys.stdin.readline().split())

graph = []
for _ in range(e):
    A, B, C = map(int, sys.stdin.readline().split())
    graph.append((A, B, C))

parent = [i for i in range(v + 1)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    parent[x] = y

graph.sort(key=lambda x: x[2])

answer = 0

for a, b, c, in graph:
    if find(a) != find(b):
        answer += c
        union(a, b)

print(answer)

'''
Spanning tree(신장 트리)
신장 트리는 하나의 그래프가 있을 때 모든 노드를 포함하면서 싸이클은 일어나지 않는 트리를 말한다.  
예를 들어 모든 네트워크를 최소 연결로 연결하려고 할 때 신장 트리를 생성할 수 있다.  

MST(Minimum Spanning Tree)
최소 신장 트리는 spanning tree 중 간선의 가중치의 합이 가장 작은 것을 말한다.  
즉 거리나 길이 등을 가중치로 했을 때 모든 노드를 연결하는 필요한 최소 자원을 만족할 때 MST가 된다.

Kruskal algorithm
그리디 알고리즘의 일종이다.  
간선의 비용이 가장 적은 것을 순서대로 나열한 다음 하나하나 이어간다.  
연결을 하다가 기존의 트리와 사이클이 만들어지면 추가 작업을 하지 않고 넘어간다.  
사이클을 만드는 과정은 union-find를 사용한다.  
부모가 같은지를 확인한 다음 부모가 같으면 사이클이 만들어지는 것이기 때문에 아무것도 하지 않고,  
부모가 다르면 사이클이 만들어지지 않기 때문에 union 과정을 거쳐 트리에 연결한다.  
트리를 하나씩 병합해나가는 과정인 것이다.
'''
