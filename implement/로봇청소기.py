import sys

H, W = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
direction = dict()
for i in range(4):
    direction[i] = (dx[i], dy[i])

def has_uncleaned(x, y):
    for i in range(4):
        if maps[x + dx[i]][y + dy[i]] == 0:
            return True
    return False

answer = 0

while True:
    if maps[r][c] == 0:
        maps[r][c] = 2
        answer += 1
        continue

    if not has_uncleaned(r, c):
        if maps[r - dy[d]][c - dx[d]] != 1:
            r, c = r - dy[d], c - dx[d]
            continue
        else:
            break
    else:
        d = (d + 3) % 4
        if maps[r + dy[d]][c + dx[d]] == 0:
            r, c = r + dy[d], c + dx[d]

print(answer)