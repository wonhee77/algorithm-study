import heapq
import sys

N = int(input())
nums = [int(sys.stdin.readline()) for _ in range(N)]
heapq.heapify(nums)

if N == 1:
    print(0)
    exit(0)

answer = 0

while len(nums) > 1:
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    answer += (a + b)
    heapq.heappush(nums, a + b)

print(answer)
