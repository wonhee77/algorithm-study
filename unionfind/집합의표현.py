import sys
sys.setrecursionlimit(10**8)
n, m = map(int, input().split())

def make_set(num):
    return [i for i in range(num + 1)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    parent[x] = y

parent = make_set(n)

for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
