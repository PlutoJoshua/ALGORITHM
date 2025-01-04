def solution(num_list):
    i=0
    j=0
    for x in num_list:
        if x % 2 ==0:
            i +=1
        else:
            j +=1
    return [i,j]
    