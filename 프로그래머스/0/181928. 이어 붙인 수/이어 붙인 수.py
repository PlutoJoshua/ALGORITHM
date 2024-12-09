def solution(num_list):
    r = ""
    r2 = ""
    for num in num_list:
        if num % 2 == 0:
            r += str(num)
        else:
            r2 += str(num)
    return int(r) + int(r2)
            