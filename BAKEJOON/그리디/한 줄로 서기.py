n = int(input())
line = list(map(int, input().split()))

ans = [0]*n
for i in range(n):
    left = line[i] #왼쪽에 자신보다 키 큰 사람의 수
    for j in range(n):
        if ans[j] == 0 and left == 0:
            ans[j] = i+1
            break
        elif ans[j] == 0 or ans[j] > i+1:
            left -= 1
for a in ans:
    print(a, end=" ")
