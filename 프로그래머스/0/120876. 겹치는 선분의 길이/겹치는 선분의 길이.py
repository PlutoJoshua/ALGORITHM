from collections import Counter
def solution(lines):
    points = []
    for line in lines:
        start, end = line
        points.extend(range(start, end))
    
    counter = Counter(points)
    
    overlap_length = sum(1 for count in counter.values() if count > 1)
    
    return overlap_length
