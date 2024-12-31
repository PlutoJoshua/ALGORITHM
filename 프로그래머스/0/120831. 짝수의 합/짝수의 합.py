def solution(n):
    sol = int(n/2)
    answer = 0
    for i in range(sol+1):
        answer += 2 * i
    return answer