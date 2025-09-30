def solution(dots):
    def slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])
    if slope(dots[0], dots[1]) == slope(dots[2], dots[3]):
        return 1
    if slope(dots[0], dots[2]) == slope(dots[1], dots[3]):
        return 1
    if slope(dots[0], dots[3]) == slope(dots[1], dots[2]):
        return 1
    
    return 0
    