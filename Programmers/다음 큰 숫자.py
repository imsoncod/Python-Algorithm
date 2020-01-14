def solution(n):
    a = bin(n).count('1')
    while 1:
        n+=1
        b = bin(n).count('1')
        if a==b:
            break
    return n
