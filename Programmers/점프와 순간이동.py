def solution(n):
    jump=0
    while n>0:
        if n%2!=0:
            n-=1
            jump+=1
        n//=2    
    return jump
