def solution(arr):
    dir = 0
    for i in arr:
        dir +=i
    return dir/len(arr)