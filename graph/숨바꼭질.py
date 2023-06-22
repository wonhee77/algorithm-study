from collections import deque

s, b = map(int, input().split())

def bfs(s):
    queue = deque([s])
    visited = [0] * 100001
    while queue:
        x = queue.popleft()
        if x == b:
            return visited[x]
        for a in (x - 1, x + 1, x * 2):
            if 0 <= a <= 100000 and not visited[a]:
                visited[a] = visited[x] + 1
                queue.append(a)

print(bfs(s))


'''
bfs를 사용하여 풀 수 있는 문제이다.
처음엔 dp를 사용하여 최소 이동값을 계산하려고 했지만 하나의 값이 바뀌면
연쇄적으로 모든 값들이 바뀔 수 있기 때문에 dp를 사용할 수 없었다.
이 문제는 사실 깊이와 관련된 문제이다. 
특정한 깊이에서 값들을 모두 찾아보고 계속 깊이를 더해가면서 먼저 답을 찾는 순간에 그 깊이를 출력한다.
'''

