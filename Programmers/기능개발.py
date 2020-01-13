"""각 작업이 개발완료되기까지 일수를 구하여 앞의 작업부터 비교해보자"""
def solution(progresses, speeds):
    answer = []
    day = [] #작업기간을 저장할 리스트
    remove_idx = [] #삭제할 작업기간의 index를 저장할 리스트
    for idx in range(len(progresses)):
        #작업기간을 계산함
        for i in range(1,100):
            if (progresses[idx]+i*speeds[idx])>=100:
                day.append(i)
                break
    while day: #작업기간이 다 사라질때까지
        cnt = 0 #배포할 기능 수
        first = day[0] #가장 앞의 작업기간값
        for i in day:
            if first >= i: #first보다 작업기간이 짧거나 같으면
                remove_idx.append(i) #제거목록에 저장
                cnt+=1 #배포할 기능수 +1
            else: #first보다 작업기간이 길면
                answer.append(cnt) #배포할 기능수를 정답에 추가
                break    
        for j in remove_idx: #제거할 day를 제거
            day.remove(j)
        remove_idx.clear() #제거목록 초기화
        if not day: #day가 다 제거됐다면(마지막 index에 도달했다면)
            answer.append(cnt) #배포할 기능수를 정답에 추가
    return answer
