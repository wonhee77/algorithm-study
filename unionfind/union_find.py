def mark_set(n):
    return [i for i in range(n)]

parent = mark_set(10)

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
    parent[y] = x


'''
union-find 알고리즘 서로소 부분집합들로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조이다.
tree 구조로 표현이 되며 find와 union을 통해 부모를 찾고 합집합 연산을 실시한다.
'''
