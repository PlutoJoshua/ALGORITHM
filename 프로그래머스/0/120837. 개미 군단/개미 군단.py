def solution(hp):
    one = hp // 5
    re_one = hp % 5
    
    two = re_one // 3
    re_two = re_one % 3
    return one + two + re_two