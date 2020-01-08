def solution(arr):
    a = [arr[0]]
    for s in arr:
        if a[-1]==s:
            continue
        a.append(s)    
    return a
