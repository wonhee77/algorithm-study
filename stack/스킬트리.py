def solution(skill, skill_trees):
    answer = 0

    for st in skill_trees:
        stack = []
        for i in range(len(skill) - 1, -1, -1):
            stack.append(skill[i])

        is_answer = True
        for s in st:
            if s == stack[-1]:
                stack.pop()
                if not stack:
                    break
            else:
                if s in stack:
                    is_answer = False
                    break
        if is_answer:
            answer += 1

    return answer