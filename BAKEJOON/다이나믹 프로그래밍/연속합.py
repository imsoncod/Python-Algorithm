n = int(input())

num = list(map(int, input().split()))

temp = 0
ans = -1000

#(전까지의 합 + 현재 수, 그냥 현재 수)를 비교
#현재 수가 더 크면 연속합을 멈추고 현재 수부터 새로 시작
for i in range(n):
    temp = max(temp+num[i], num[i])
    ans = max(ans, temp)

print(ans)
