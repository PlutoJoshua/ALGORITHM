def solution(numbers):
    sort = sorted(numbers)
    answer = sort[-1] * sort[-2]
    return answer