def solution(stones, k):
    low = 0
    high = 200000000

    while low <= high:
        mid = (low + high) // 2
        row = 0
        for stone in stones:
            if stone <= mid:
                row += 1
                if row == k:
                    break
            else:
                row = 0

        if row == k:
            high = mid - 1
        else:
            low = mid + 1

    return low

# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

"""
쉽게 생각하면 모든 징검다리의 숫자를 -1 하면서 0이 k번 이상 나오기 위해 몇번을 빼야되는지를 구하면 된다.
하지만 돌다리의 최대값이 2억이기 때문에 모든 돌다리가 2억일 경우 최대 20만개의 돌다리마다 빼기 연산을 2억번 해야될 수도 있다.
2억 X 20만 번의 연산을 해야되기 때문에 효율성 측면에서 좋지 않다.
이 연산을 줄이기 위해 이진탐색을 사용한다. O(logN)의 시간 복잡도로 계산할 수 있다.
"""