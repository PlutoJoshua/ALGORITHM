def solution(sides):
    answer = 0
    return 1 if max(sides) < sum(sorted(sides)[:2]) else 2