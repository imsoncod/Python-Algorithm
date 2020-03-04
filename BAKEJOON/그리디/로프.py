n = int(input())

arr=[]
for _ in range(n):
    arr.append(int(input()))
#내림차순 정렬
arr = sorted(arr, key=lambda x:-x)

#높은 무게부터 로프를 1,2,3...n개씩 사용할 때 가장 적은 무게를 견디는 로프 무게에 로프 개수만큼 곱해준다
#5 4 3 2 1일경우
#5
#4*2
#3*3
#2*4
#1*5

ans = arr[0]
for i in range(1, n):
    ans = max(ans, arr[i]*(i+1))
print(ans)
