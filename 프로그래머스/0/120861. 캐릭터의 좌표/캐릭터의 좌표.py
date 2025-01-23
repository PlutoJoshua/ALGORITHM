def solution(keyinput, board):
    x, y = 0, 0
    x_limit = board[0]//2
    y_limit = board[1]//2
    for i in keyinput:
        if i =="left":
            x -=1
        elif i =="right":
            x +=1
        elif i =="up":
            y +=1
        else:
            y -=1
        x = max(-x_limit, min(x, x_limit))
        y = max(-y_limit, min(y, y_limit))
    return [x, y]