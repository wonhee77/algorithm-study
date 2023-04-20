def solution(n, computers):
    visited = [False] * n
    answer = 0

    def dfs(start):
        network = computers[start]
        for i in range(len(network)):
            if (network[i] == 0) | (start == i):
                continue
            if not visited[i]:
                visited[i] = True
                dfs(i)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))