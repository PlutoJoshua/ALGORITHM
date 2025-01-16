def solution(order):
    answer = 0
    response = ["3", "6", "9"]
    for i in str(order):
        if i in response:
            answer +=1
    return answer