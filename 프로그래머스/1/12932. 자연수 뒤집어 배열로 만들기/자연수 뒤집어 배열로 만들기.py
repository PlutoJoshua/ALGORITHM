def solution(n):
    answer = []
    for a in str(n)[::-1]:
        answer.append(int(a))
    return answer