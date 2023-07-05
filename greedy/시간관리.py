import sys

N = int(input())
arr = []
for _ in range(N):
    t, s = map(int, sys.stdin.readline().split())
    arr.append((t, s))

arr.sort(key=lambda x: -x[1])
rest_time = arr[0][1]

for a in arr:
    t = a[0]
    s = a[1]
    if s >= rest_time:
        rest_time -= t
    else:
        rest_time = s - t

print(rest_time if rest_time >= 0 else -1)