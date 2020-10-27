# O(N+K)
# 데이터가 0,999999 2개일 경우 매우 비효율적
# 동일한 값을 데이터가 여러 개 등장할 때 효율적

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
