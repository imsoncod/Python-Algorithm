def solution(num):
    cnt = 0
    while(num!=1):
        if(num%2==0):
            num = num/2
        else: num = num*3+1
        #위 과정을 반복하면 모든 수를 1로 만들 수 있다는 추측이다
        if(cnt!=500):
            cnt+=1
        else: return -1
    return cnt
