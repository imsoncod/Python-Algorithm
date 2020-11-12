n = int(input())
arr = list(map(int, input().split()))
m = int(input())
request = list(map(int, input().split()))

arr.sort()

for req in request:
    left = 0
    right = n-1

    check = False
    while left <= right:
        #인덱스를 기준으로 잡는다
        mid = (left+right)//2

        if req == arr[mid]:
            check = True
            print("yes")
            break
        elif req > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    if check == False:
        print("no")
