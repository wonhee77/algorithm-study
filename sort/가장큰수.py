def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))


'''
파이썬 정렬할 때 key를 이용하면 변형을 통한 값을 바로 정렬할 수 있다.
! 미리 값을 조작해놓을 필요 없음
! 파이썬에서 문자열 정렬은 왼쪽부터 아스키로 비교한다.
'''