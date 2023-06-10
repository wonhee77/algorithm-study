def solution(numbers):
    answer = []

    for num in numbers:
        bnum = bin(num)[2:]
        cnt = 0
        for i in range(1, len(bnum) + 1):
            if bnum[i * -1] == '1':
                cnt += 1
                continue
            break

        if cnt >= 2:
            answer.append(num + pow(2, cnt - 1))
        else:
            answer.append(num + 1)

    return answer
