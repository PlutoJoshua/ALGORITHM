def solution(board):
    n = len(board)
    danger = [[0]*n for _ in range(n)]
    
    dir = [(-1, -1), (-1,0), (-1,1),
           (0,-1), (0,0), (0,1),
           (1,-1), (1,0), (1,1)
          ]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] ==1:
                for x, y in dir:
                    a, b = i+x, j+y
                    if 0 <=a <n and 0 <= b <n:
                        danger[a][b] = 1
                        
    safe = 0
    for i in range(n):
        for j in range(n):
            if danger[i][j] == 0:
                safe += 1
    
    return safe