from collections import Counter

def solution(array):
    counter = Counter(array)
    max_count = max(counter.values())
    
    modes = [i for i, count in counter.items() if count == max_count]
    
    if len(modes) >1:
        return -1
    return modes[0]
            