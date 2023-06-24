import sys
from collections import deque

test_count = int(sys.stdin.readline())

for _ in range(test_count):
    command = sys.stdin.readline()
    length = int(sys.stdin.readline())
    queue = deque(sys.stdin.readline().lstrip('[').rstrip('\n').rstrip(']').split(','))
    if length == 0:
        queue = deque()

    reverse = False
    error = False
    for c in command:
        if c == 'R':
            if reverse:
                reverse = False
            else:
                reverse = True
        if c == 'D':
            if not queue:
                error = True
                break
            if reverse:
                queue.pop()
            else:
                queue.popleft()

    if error:
        print('error')
    else:
        if reverse:
            queue.reverse()
            print('[' + ','.join(queue) + ']')
        else:
            print('[' + ','.join(queue) + ']')

