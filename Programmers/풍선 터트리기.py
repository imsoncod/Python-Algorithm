#풀이
#선택된 수를 기준으로 양쪽을 분할탐색한다
#A B C
#A,C리스트에서 인접한 두 수 중에서 큰 수 만을 없애다 보면 결국에는 최솟값만 남을 것이다
#min_A, B, min_C로 세 수가 남았을 때
#조건에 의해 min_A, min_C 두 수 모두 B보다 작다면 B는 살아남을수 없다
#반면 min_A, mic_C중 "하나"라도 B보다 크다면 B는 살아남을수 있다 -> 요게 메인
#---------------------------------------------------------
#min함수를 사용하면 시간초과가 뜬다

def solution(a):
    answer = 2
    n = len(a)
    if 0 < n < 3:
        return n

    left = a[0]
    right = a[-1]

    #양쪽중 한쪽 리스트에서만이라도 최소값이 자신보다 크다면 무조건 산다!
    for i in range(1, n-1):
        #좌측 리스트 중 최소값이 자신보다 크면 살아남을 수 있다
        if left > a[i]:
            left = a[i]
            answer += 1
        #우측 리스트 중 최소값이 자신보다 크면 살아남을 수 있다
        if right > a[-1-i]:
            right = a[-1-i]
            answer += 1
    #중복 제거
    if left == right:
        answer -= 1   
    return answer
