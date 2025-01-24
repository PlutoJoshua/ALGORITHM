def solution(dots):
    x = [i[0] for i in dots]
    y = [i[1] for i in dots]
    
    w = max(x) - min(x)
    h = max(y) - min(y)
    
    return w * h