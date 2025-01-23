def solution(sides):
    answer = 0
    sides.sort()
    i, j = sides[0], sides[1]
    sol1 = i + j - 1
    sol2 = j - i + 1
    return sol1 - sol2 + 1