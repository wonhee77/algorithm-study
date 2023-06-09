def solution(numbers, target):
    return dfs(0, numbers, target, 0)


def dfs(idx, numbers, target, result):
    if idx == len(numbers):
        if target == result:
            return 1
        else:
            return 0
    else:
        return dfs(idx + 1, numbers, target, result + numbers[idx]) + dfs(idx + 1, numbers, target, result - numbers[idx])