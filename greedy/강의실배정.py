import sys
import heapq

N = int(input())
times = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
times.sort(key=lambda x: x[0])

queue = []
answer = 0

for time in times:
    while queue and queue[0] <= time[0]:
        heapq.heappop(queue)
    heapq.heappush(queue, time[1])
    answer = max(answer, len(queue))

print(answer)
