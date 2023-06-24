import sys
from collections import deque

test_count = int(sys.stdin.readline())

for _ in range(test_count):
    command = sys.stdin.readline()
    length = int(sys.stdin.readline())
    arr = sys.stdin.readline()[1:-2]
    queue = deque()
    if arr != '':
        a = list(map(int, arr.split(',')))
        for b in a:
            queue.append(b)
    command = command.replace('RR', '')
    error = False
    for i in range(len(command)):
        c = command[i]
        if c == 'R':
            queue.reverse()
        if c == 'D':
            if not queue:
                error = True
                break
            queue.popleft()
    if error:
        print('error')
    else:
        answer = '['
        while queue:
            num = queue.popleft()
            answer += str(num)
            if queue:
                answer += ','
        answer += ']'
        print(answer)
