def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if all(j in "05" for j in str(i)):
               answer.append(i)
    if not answer:
        return [-1]
    return answer