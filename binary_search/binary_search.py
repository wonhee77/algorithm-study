def solution(target, arr):
    answer = -1
    arr.sort()  # 오름차순으로 정렬 필요
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            answer = mid + 1
            break
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return answer


print(solution(7, [1, 4, 5, 7, 10, 11, 15, 21, 25]))  # 4
print(solution(7, [1, 4, 5, 10, 11, 15, 21, 25]))  # -1
