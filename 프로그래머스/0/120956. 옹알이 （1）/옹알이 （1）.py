def solution(babbling):
    count = 0
    answer = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for j in answer:
            while j in i:
                i = i.replace(j, " ", 1)
        if i.strip() == "":
            count += 1
            
    return count
