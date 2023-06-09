import heapq

def solution(scoville, K):
    sco = scoville
    heapq.heapify(sco)
    count = 0

    while sco[0] < K:
        a = heapq.heappop(sco)
        b = heapq.heappop(sco)
        new = a + 2 * b
        heapq.heappush(sco, new)
        count += 1
        if len(sco) == 1:
            if sco[0] >= K:
                return count
            else:
                return -1
    return count