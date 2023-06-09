def solution(n):
    a = 1
    b = 2
    if n <= 2:
        return n

    for i in range(3, n + 1):
        tmp = b
        b = (a + b) % 1000000007
        a = tmp

    return b


'''
계단 오르기와 같은 문제이다.
모양이 반복되는 경우 점화식을 생각해보자.
현재는 바로 전 + 세로 1칸 짜리와 2번째 전에서 가로 2칸 짜리를 오른 것과 같다.
처음에는 dp 배열에 넣어서 풀었으나 간단한 문제로 점화식만으로 풀 수 있다.
'''