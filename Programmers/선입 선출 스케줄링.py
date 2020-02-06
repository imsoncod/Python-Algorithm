#효율성 테스트 실패... Parametric Search 이용해서 다시 풀어보기
def solution(n, cores):
    time = 0
    while n>0:
        for i in range(0,len(cores)):
            if time%cores[i]==0:
                n-=1
                if n==0:
                    return i+1
        time+=1
