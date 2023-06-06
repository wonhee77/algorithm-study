def solution(m, n, board):
    bo = []
    for i in board:
        bo.append(list(i))
    last_board = pang(m,n,bo, False)
    answer = 0
    for i in last_board:
        answer += i.count(0)

    return answer

def pang(m, n , board, end):
    if end:
        return board
    end = True
    removed = []
    for i in range(m -1):
        for j in range(n -1):
            if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1] != 0:
                removed += [[i, j], [i + 1, j], [i, j + 1], [i + 1, j + 1]]
                end = False
    for [i,j] in removed:
        board[i][j] = 0
    for i in range(m -1 ,-1, -1):
        for j in range(n):
            if board[i][j] == 0:
                for k in range(i - 1, -1 , -1):
                    if board[k][j] != 0:
                        board[i][j] = board[k][j]
                        board[k][j] = 0
                        break
    return pang(m, n, board, end)