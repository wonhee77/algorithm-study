import sys

T = int(input())
for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    str_arr = sys.stdin.readline().rstrip()
    arr = list(
        map(int, str_arr[1:-1].split(','))) if str_arr != '[]' else list()
    start_left = True
    length = len(arr)
    del_left, del_right = 0, 0
    error = False
    for command in p:
        if command == 'R':
            start_left = not start_left
        else:
            if length == 0:
                error = True
                break
            if start_left:
                del_left += 1
            else:
                del_right += 1
            length -= 1
    if error:
        print('error')
    else:
        arr = arr[del_left: len(arr) - del_right]
        if not start_left:
            arr.reverse()
        print('[' + ','.join(map(str, arr)) + ']')
