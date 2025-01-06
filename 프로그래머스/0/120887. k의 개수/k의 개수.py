def solution(i, j, k):
    count = 0
    for x in range(i,j+1):
        count += str(x).count(str(k))
    return count