def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            pop = stack.pop()
            answer[pop] = i - pop
        stack.append(i)

    for j in stack:
        answer[j] = len(prices) - j - 1

    return answer


'''
stack을 사용하여 풀이 진행
가장 쉬운 방법은 index의 값을 하나씩 탐색하며 이중 for문을 통해 현재 가격보다 낮아지는 시점을 찾으면 된다.
하지만 뒷쪽에 있는 값일수록 조회가 여러번 되기 때문에 효율성에서 떨어진다고 판단 
이전값보다 값이 떨어지지 않는다면 계속 진행이 될 것이고 결론적으로 트리거는 값이 떨어질 때이다.
stack에 쌓인 값은 오름차순이기 때문에 떨어질때의 값을 기준으로 하나씩 빼며 값을 비교하고 stack의 상단의 값이 
트리거가 발생한 값보다 작으면 stack 상단의 값의 index의 가격 유지 기간을 알 수 있다.
 * 트리거 포인트를 생각하자!
'''
