def solution(a, b, c, d):
    dice = [a, b, c, d]
    freq = sorted([dice.count(x) for x in set(dice)])
    unique = list(set(dice))

    if freq == [4]: 
        return 1111 * unique[0]
    elif freq == [1, 3]: 
        p, q = unique
        p, q = (p, q) if dice.count(p) > dice.count(q) else (q, p)
        return (10 * p + q) ** 2
    elif freq == [2, 2]: 
        return (unique[0] + unique[1]) * abs(unique[0] - unique[1])
    elif freq == [1, 1, 2]:
        p = unique[[dice.count(x) for x in unique].index(2)]
        q, r = [x for x in unique if dice.count(x) == 1]
        return q * r
    else:
        return min(dice)