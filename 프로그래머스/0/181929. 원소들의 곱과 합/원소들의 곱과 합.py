def solution(num_list):
    r = 1
    for num in num_list:
        r *= num
    return 1 if r < sum(num_list) **2 else 0