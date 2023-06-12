def solution(topping):
    answer = 0
    forward = []
    backward = []
    fs = set()
    bs = set()

    for i in range(len(topping)):
        f = topping[i]
        b = topping[len(topping) - i - 1]
        if f in fs:
            forward.append(forward[-1])
        else:
            fs.add(f)
            if not forward:
                forward.append(1)
            else:
                forward.append(forward[-1] + 1)
        if b in bs:
            backward.append(backward[-1])
        else:
            bs.add(b)
            if not backward:
                backward.append(1)
            else:
                backward.append(backward[-1] + 1)

    backward.reverse()

    for i in range(len(forward) - 1):
        if forward[i] == backward[i + 1]:
            answer += 1

    return answer

from collections import Counter

def solution(topping):
    answer = 0
    dic = Counter(topping)
    set_dic = set()
    answer = 0

    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            answer += 1

    return answer


'''
Dictionary를 활용한 문제이다.
처음에 푼 버전은 앞에서부터 숫자의 누적된 개수와 뒤에서부터 숫자의 누적 개수를 각각 저장한다.
그리고 index를 훑으면서 값을 비교해 같은 값이 있으면 답으로 인정한다.

두번째 버전은 dictionary를 활용한 방법이다.
처음부터 개수를 모두 세어서 dictionary에 저장한 다음
숫자를 하나하나씩 set에는 넣고 dictionary에서 빼면서 각각 길이를 비교해 같은 경우 답으로 인정한다.

두 방법 다 시간은 비슷하게 나왔지만 Counter를 사용함으로써 두번째 방법이 코드상으로는 깔끔하나 첫번째 방법도
개념적으로는 나쁘지 않은 것 같다.
'''