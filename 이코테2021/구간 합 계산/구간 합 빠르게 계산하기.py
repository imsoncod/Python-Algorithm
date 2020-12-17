#구간 합 빠르게 계산하기
n = 5
data = [10,20,30,40,50]

sum_value = 0
sum_list = [0] #초기값 0을 두어야함

for d in data:
    sum_value += d
    sum_list.append(sum_value)

#sum_list = [0,10,30,60,100,150]

#두번째수부터 네번째수 까지의 합
#20+30+40 = 90
a = 2
b = 4

#arr[b] - arr[a-1]
print(sum_list[b] - sum_list[a-1])
