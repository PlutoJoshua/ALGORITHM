def solution(my_string):
    answer = 0
    char = 0
    for i in my_string:
        if i.isdigit():
            char = char *10 + int(i)
        else:
            answer += char
            char =0
    answer +=char
    return answer