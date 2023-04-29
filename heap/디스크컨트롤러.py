import heapq

def solution(jobs):
    total = len(jobs)
    total_sum, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < total:
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, (job[1], job[0]))
        if heap:
            d, s = heapq.heappop(heap)
            start = now
            now += d
            total_sum += now - s
            i += 1
        else:
            now += 1

    return int(total_sum / total)

print(solution([[0, 3], [1, 9], [2, 6]]))
