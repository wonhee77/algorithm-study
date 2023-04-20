def solution(begin, target, words):
    answer = float('inf')
    word_len = len(begin)
    visited = [False] * len(words)
    def dfs(word, depth):
        nonlocal answer
        if word == target:
            answer = min(answer, depth)
        for i in range(len(words)):
            if visited[i]:
                continue
            cnt = 0
            print(word, words[i], depth)
            for j in range(word_len):
                if word[j] != words[i][j]:
                    cnt += 1
            if cnt == 1:
                visited[i] = True
                dfs(words[i], depth + 1)
                visited[i] = False

    dfs(begin, 0)

    return answer if answer != 100 else 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
