def convert(n, num):
    stack = []
    nums = "0123456789ABCDEF"
    while True:
        mok, rest = divmod(num, n)
        if mok == 0 and rest == 0:
            break
        num = mok
        stack.append(nums[rest])
    answer = ''
    while stack:
        answer += stack.pop()
    return answer


def solution(n, t, m, p):
    max_num = t * m
    str_num = '0'

    num = 1
    while True:
        str_num += convert(n, num)
        if len(str_num) > max_num:
            break
        num += 1

    answer = ''

    idx = p
    while len(answer) != t:
        answer += str_num[idx - 1]
        idx += m

    return answer