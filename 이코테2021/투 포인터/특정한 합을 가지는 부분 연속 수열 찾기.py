#투 포인터 알고리즘
n = 5 #데이터의 개수
m = 5 #찾고자하는 부분합
data = [1,2,3,2,5]

cnt = 0
interval_sum = 0
end = 0

#start와 end를 인덱스로하여 부분합을 구한다
#start가 증가한다는 것은 범위의 감소를 의미함과 동시에 부분합의 감소를 의미한다
#end가 증가한다는 것은 범위의 증가를 의미함과 동시에 부분합의 증가를 의미한다

for start in range(n):
    #찾고자하는 부분합에 도달할때까지 end의 값을 증가시킨다 = 부분합의 값을 증가시킨다
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    #값을 찾으면 cnt를 증가시킨다
    if interval_sum == m:
        cnt += 1
    #for문이 한 번 실행될때마다 start가 증가함으로 data[start]를 빼준다
    interval_sum -= data[start]

print(cnt)
