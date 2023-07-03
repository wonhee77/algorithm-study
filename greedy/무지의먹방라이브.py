import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    food = []
    for i in range(len(food_times)):
        heapq.heappush(food, [food_times[i], i + 1])

    previous = 0

    while (food[0][0] - previous) * len(food) <= k:
        k -= (food[0][0] - previous) * len(food)
        previous = food[0][0]
        heapq.heappop(food)

    food.sort(key=lambda x: x[1])

    k = k % len(food)

    return food[k][1]

'''
그리디 알고리즘 문제이다.
시간이 지나면서 하나씩 먹으면 k 만큼의 시간이 든다.
이때 먹는데 시간이 가장 적게 걸리는 음식을 기준으로 한번에 먹어가면 시간을 줄일 수 있다.
먹는데 가장 적은 시간이 걸리는 음식부터 먹는것이 현재 상황에서 최선의 상황이자 전체로 봤을 때도 최선의 선택!
'''