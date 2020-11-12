n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

#같은 수라도 다른 인덱스의 수는 다른걸로 판단하기 때문에
#정렬하여 가장 큰 순서대로 2개의 수만 뽑아내면 된다

arr.sort();
firstMax = arr[-1]
secondMax = arr[-2]

answer = 0
while True:
    for i in range(k):
        if m == 0:
            break
        answer += firstMax
        m -= 1
    if m == 0:
        break
    answer += secondMax
    m -= 1

print(answer)
