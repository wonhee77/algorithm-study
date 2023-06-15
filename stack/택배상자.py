from collections import deque

def solution(order):
    new_order = [0] * len(order)
    for i in range(len(order)):
        new_order[order[i] - 1] = i + 1

    new_order = deque(new_order)
    stack = []
    now = 1

    while True:
        if stack and stack[-1] == now:
            stack.pop()
            now += 1
            continue

        if not new_order:
            break

        candidate = new_order.popleft()
        if candidate == now:
            now +=1
        else:
            stack.append(candidate)

    return len(order) - len(stack)