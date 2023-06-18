from collections import deque


def bfs(num, graph, visited):
    queue = deque([num])
    count = 0
    while queue:
        a = queue.popleft()
        if visited[a]:
            continue
        visited[a] = True
        count += 1
        for b in graph[a]:
            queue.append(b)
    return count


def solution(n, wires):
    answer = float('inf')
    for i in range(n - 1):
        new_wire = wires[:i] + wires[i + 1:]
        visited = [False] * (n + 1)
        graph = [[] for _ in range(n + 1)]
        nums = []
        for w in new_wire:
            graph[w[0]].append(w[1])
            graph[w[1]].append(w[0])
        for key in range(1, n + 1):
            if visited[key]:
                continue
            nums.append(bfs(key, graph, visited))
            print(key)
        if len(nums) == 1:
            nums.append(1)
        answer = min(answer, abs(nums[0] - nums[1]))

    return answer


'''
BFS를 이용한 완전 탐색 문제이다. graph를 dictionary 형태로도 표현할 수 있지만
값을 꺼내고 넣는 등의 행위 없이 참고만 할 경우 이중 list를 이용하여
각각의 index를 key 값으로 사용할 수도 있다.
'''