def solution(n):
    if n % 2 != 0:
        return sum(i for i in range(1, n + 1, 2))
    else:
        return sum(j ** 2 for j in range(2, n + 1, 2))