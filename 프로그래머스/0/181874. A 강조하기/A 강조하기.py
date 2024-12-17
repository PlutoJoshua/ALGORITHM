def solution(myString):
    result = ''
    for i in myString:
        if i =='a':
            result += 'A'
        elif i.upper() and i != 'A':
            result +=i.lower()
        else:
            result += i
    return result