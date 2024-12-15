def solution(myString):
    return list(sorted(filter(lambda x: x!="", myString.split("x"))))