def solution(m, s, e):
    return m[:s] + m[s:e+1][::-1] + m[e+1:]