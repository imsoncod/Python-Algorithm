from math import sqrt

def solution(begin, end):
    ans = []
    for n in range(begin, end+1):
        if n == 1:
            ans.append(0)
            continue
        #2부터 제곱근까지 각각의 수로 나누어 떨어지지 않으면 소수
        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                ans.append(n//i)
                break
        else:
            ans.append(1)
    return ans
