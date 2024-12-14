def solution(my_string, is_suffix):
    str = []
    for i in range(len(my_string)):
        str.append(my_string[i:])
    if is_suffix in str:
        return 1
    else:
        return 0