def solution(my_string):
    value = "aeiou"
    return ''.join(i for i in my_string if i not in value)