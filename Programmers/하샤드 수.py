def solution(x):
    return x%sum(map(int,str(x)))==0
    #자리수의 합으로 자신이 나누어 떨어지면 하샤드 수
