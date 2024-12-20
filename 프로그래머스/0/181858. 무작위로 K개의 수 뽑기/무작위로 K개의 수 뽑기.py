def solution(arr, k):
    unique = list(dict.fromkeys(arr))
    result = unique[:k]
    result += [-1] * (k - len(result))
    return result