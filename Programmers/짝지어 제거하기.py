def solution(s):
    stack = []
    s = list(s)
    for i in range(len(s)):
        stack.append(s[i])
        if len(stack)>1:
            if stack[-1]==stack[-2]:
                stack.pop()
                stack.pop()        
    return 1 if len(stack)==0 else 0
