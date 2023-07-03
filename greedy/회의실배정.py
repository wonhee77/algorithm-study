N = int(input())

meeting = [list(map(int, input().split())) for _ in range(N)]
meeting.sort(key=lambda x: (x[1], x[0]))

end = meeting[0][1]
answer = 1

for i in range(1, len(meeting)):
    if meeting[i][0] >= end:
        answer += 1
        end = meeting[i][1]

print(answer)