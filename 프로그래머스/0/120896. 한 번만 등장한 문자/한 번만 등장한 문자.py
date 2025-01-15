from collections import Counter
def solution(s):
    counter = Counter(s)
    
    return ''.join(sorted(i for i, count in counter.items() if count ==1))