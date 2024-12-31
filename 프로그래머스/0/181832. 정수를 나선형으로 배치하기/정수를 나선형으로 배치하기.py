def solution(n):
    spiral = [[0] * n for _ in range(n)]
    dir = [(0,1), (1,0), (0,-1), (-1,0)]
    curr_dir = 0
    x, y = 0,0
    num = 1

    while num <= n*n:
        spiral[x][y] = num
        num += 1
        next_x = x + dir[curr_dir][0]
        next_y = y + dir[curr_dir][1]
        
        if 0 <=next_x < n and 0 <= next_y < n and spiral[next_x][next_y] == 0:
            x, y = next_x, next_y
        else:
            curr_dir = (curr_dir + 1) % 4
            x += dir[curr_dir][0]
            y += dir[curr_dir][1]
            
    return spiral
