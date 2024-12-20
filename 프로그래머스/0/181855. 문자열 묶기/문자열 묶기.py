def solution(strArr):
    leng_counts = {}
    
    for i in strArr:
        leng = len(i)
        leng_counts[leng] = leng_counts.get(leng, 0) + 1
    return max(leng_counts.values())
