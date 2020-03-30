ans = 0
n, k = map(int, input().split())
arr = list(map(int, input().split()))
multi = [0]*n

for i in range(k):
    if arr[i] in multi: #멀티탭에 이미 꽂혀 있는가
        continue
    elif 0 in multi: #멀티탭에 비어있는 곳이 있는가
        multi[multi.index(0)] = arr[i]
        continue
    #멀티탭에 꽂을 곳이 없는가
    ans+=1

    select = False
    # 후에 사용할 일이 없는것부터
    for j in range(n):
        if multi[j] not in arr[i+1:]:
            multi[j] = arr[i]
            select = True
            break
    #뽑아냈으면
    if select:
        continue

    #후에 처음으로 사용되는 시점이 가장 늦는 것부터
    idx = 0
    for j in range(n):
        idx = max(idx, arr[i+1:].index(multi[j]))
    multi[multi.index(arr[i+1+idx])] = arr[i]

print(ans)
