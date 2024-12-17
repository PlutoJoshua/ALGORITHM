def solution(num_list):
    if len(num_list) > 10:
        return(sum(num_list))
    else:
        result = 1
        for i in num_list:
            result *= i
        return result