def solution(arr, queries):
    result = []
    for s, e, k in queries:
        filtered = [arr[i] for i in range(s, e + 1) if arr[i] > k]
        
        if filtered:
            result.append(min(filtered))
        else:
            result.append(-1)
    return result