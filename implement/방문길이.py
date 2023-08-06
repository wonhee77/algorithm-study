def solution(dirs):
    root = set()
    x, y = 0, 0

    for d in dirs:
        new_x, new_y = x, y
        if d == 'U' :
            new_y += 1
        if d == 'L' :
            new_x -= 1
        if d == 'R' :
            new_x += 1
        if d == 'D' :
            new_y -= 1

        if -5 <= new_x <= 5 and -5 <= new_y <= 5:
            root.add(str(x) + str(y) + str(new_x) + str(new_y))
            root.add(str(new_x) + str(new_y) + str(x) + str(y))
            x, y = new_x, new_y

    return len(root) // 2