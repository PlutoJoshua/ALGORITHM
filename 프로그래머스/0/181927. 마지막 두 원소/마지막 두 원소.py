def solution(n):
    return n + [n[-1] - n[-2] if n[-1] > n[-2] else n[-1] * 2]

