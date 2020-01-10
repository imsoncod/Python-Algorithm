import itertools

def solution(baseball):
    num = list(map(''.join,itertools.permutations(list(map(str,list(range(1,10)))),3)))
    cnt = 0
    for j in num:
        check = len(baseball)
        for i in baseball:
            strike = 0
            ball = 0
            if str(i[0])[0]==j[0]:
                strike+=1
            elif str(i[0])[0]==j[1] or str(i[0])[0]==j[2]:
                ball += 1
            if str(i[0])[1]==j[1]:
                strike+=1
            elif str(i[0])[1]==j[0] or str(i[0])[1]==j[2]:
                ball += 1    
            if str(i[0])[2]==j[2]:
                strike+=1
            elif str(i[0])[2]==j[0] or str(i[0])[2]==j[1]:
                ball += 1      
            if i[1]==strike and i[2]==ball:
                check-=1
                if check==0:
                    cnt+=1
    return cnt
