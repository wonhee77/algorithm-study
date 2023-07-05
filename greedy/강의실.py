# import sys
# import heapq

# N = int(input())
# times = []
#
# for _ in range(N):
#     n, s, e = map(int, sys.stdin.readline().split())
#     times.append((s, e))
#     times.append((e, s))
#
# times.sort(key=lambda x: (x[0], x[1]))
#
# answer = 0
# current_max = 0
#
# for time in times:
#     if time[0] < time[1]:
#         current_max += 1
#         answer = max(answer, current_max)
#     else:
#         current_max -= 1
#
# print(answer)

import sys
import heapq

N = int(input())
times = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
times.sort(key=lambda x: x[1])

queue = []
answer = 0

for time in times:
    while queue and queue[0] <= time[1]:
        heapq.heappop(queue)
    heapq.heappush(queue, time[2])
    answer = max(answer, len(queue))

print(answer)

'''
첫 풀이는 단순하게 시작과 종료 시간일때마다 이벤트가 발생하므로 시작과 종료를 뒤집어 같은 강의를 중복해서 
리스트로 만들었다. 그리고 그 리스트를 순회하면서 종료면 -1, 시작이면 +1 하며 max값을 찾았다.

두번째는 시작 시간순으로 강의를 정렬하고 강의를 순회하면서 종료 시간을 heap에 넣어준다.
그리고 다음 강의를 확인할 때 만약 강의 시작 시간보다 종료 시간이 더 빠른게 있으면 heap에서 빼준다.
이때 heap의 크기가 새로운 강의가 추가되었을 때 현재 사용중인 강의 개수이다.
'''