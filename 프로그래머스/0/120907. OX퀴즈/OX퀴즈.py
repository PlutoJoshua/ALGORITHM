def solution(quiz):
    answer = []
    for i in quiz:
        x, a, y, _, z = i.split()
        if a == '+':
            o = int(x) + int(y) == int(z)
        elif a == '-':
            o = int(x) - int(y) == int(z)
        answer.append("O" if o else "X")
    return answer