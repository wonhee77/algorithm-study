N, K = map(int, input().split())
str_num = input()
stack = [int(str_num[0])]

for i in range(1, len(str_num)):
    num = int(str_num[i])
    while stack and K != 0 and stack[-1] < num:
        stack.pop()
        K -= 1
    stack.append(num)

if K != 0:
    stack = stack[:-K]

print(''.join(map(str, stack)))
