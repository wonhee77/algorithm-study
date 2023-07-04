import sys
import heapq

N, K = map(int, input().split())

jem = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = [int(sys.stdin.readline().rstrip()) for _ in range(K)]
jem.sort()
bags.sort()

answer, idx, previous_max = 0, 0, 0
max_val = []

for bag in bags:
    while idx < len(jem) and bag >= jem[idx][0]:
        heapq.heappush(max_val, -jem[idx][1])
        idx += 1
    if max_val:
        answer -= heapq.heappop(max_val)

print(answer)



