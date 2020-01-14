def solution(s):
    temp = 0
    for i in s:
        if i == '(':
            temp +=1
        else:
            temp -=1
        if temp < 0:
            break        
    return True if temp==0 else False
