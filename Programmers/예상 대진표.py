def solution(n,a,b):
    vs = 0
    while a!=b:
        a = (a+1)//2
        b = (b+1)//2
        vs+=1
    return vs
