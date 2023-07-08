import sys

N, K = map(int, input().split())
stuff = [[0, 0]]

for _ in range(N):
    stuff.append(list(map(int, sys.stdin.readline().split())))

knapsack = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0]
        value = stuff[i][1]
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
            continue
        knapsack[i][j] = max(knapsack[i - 1][j - weight] + value, knapsack[i - 1][j])

print(knapsack[N][K])