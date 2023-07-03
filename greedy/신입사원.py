import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    candidate = []
    for _ in range(N):
        candidate.append(list(map(int, sys.stdin.readline().split())))
    candidate.sort()

    answer = 1

    min_rank = candidate[0][1]
    for i in range(1, len(candidate)):
        if candidate[i][1] < min_rank:
            answer += 1
            min_rank = candidate[i][1]
    print(answer)
