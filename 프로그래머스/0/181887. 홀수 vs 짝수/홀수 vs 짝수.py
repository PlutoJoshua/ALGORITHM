def solution(num_list):
    a = 0
    b = 0
    for idx, i in enumerate(num_list):
        if idx % 2 == 0:
            a += i
        else:
            b += i
    return a if a > b else b