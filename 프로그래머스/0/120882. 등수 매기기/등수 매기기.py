def solution(score):
    average = [(i[0]+i[1])/2 for i in score]
    return [sorted(average, reverse = True).index(j) +1 for j in average]