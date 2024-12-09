def solution(a, b, c):
    result = ""
    if a == b == c:
        result = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif a != b and b != c and a!=c:
        result = a+b+c
    else:
        result = (a+b+c)*(a**2+b**2+c**2)
    return result