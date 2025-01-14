def solution(array):
    max_a = max(array)
    return [max(array), array.index(max_a)]