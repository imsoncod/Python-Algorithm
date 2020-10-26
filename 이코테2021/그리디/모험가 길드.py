def solution(n, data):
    answer = 0 #총 그룹의 수
    cnt = 0 #현재 그룹에 포함된 모험가의 수
    data.sort() #오름차순 정렬

    for i in data:
        cnt += 1 #현재 그룹에 해당 모험가를 포함 시킴
        if cnt >= i: #현재 그룹에 포함된 모험가의 수가 해당 모험가의 공포도 이상이라면
            answer += 1 #그룹 생성
            cnt = 0 #현재 그룹에 포함된 모험가의 수 초기화

    return answer

print(solution(5, [2,3,1,2,2]))
