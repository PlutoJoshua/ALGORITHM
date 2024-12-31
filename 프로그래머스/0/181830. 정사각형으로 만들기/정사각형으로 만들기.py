def solution(arr):
    row = len(arr)
    col = len(arr[0])
    
    n = max(row, col)
    
    for i in range(row):
        arr[i] += [0] * (n - col)
        
    for _ in range(n - row):
        arr.append([0]*n)
    return arr
