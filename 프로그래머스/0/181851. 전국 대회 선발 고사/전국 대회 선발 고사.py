def solution(rank, attendance):
    eligible_students = [(rank[i], i) for i in range(len(rank)) if attendance[i]]
    eligible_students.sort()
    top_three = [student[1] for student in eligible_students[:3]]
    return 10000 * top_three[0] + 100 * top_three[1] + top_three[2]
    
    