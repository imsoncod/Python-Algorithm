#permutations과 combinations의 결과는 tuple로 반환된다
#문제유형은 그리디 이지만 완전탐색으로 푼 기분
#백트래킹을 이용할 수도 있다고 한다
from itertools import permutations as pm
k = int(input())
op = input().split()
a = list(range(9,-1,-1)) #[9,8,7,6,5,4,3,2,1,0]
b = list(range(0,10)) #[0,1,2,3,4,5,6,7,8,9]

for num in pm(a,k+1):
    check = True
    for i in range(k):
        if op[i] == '<' and num[i] > num[i + 1]:
            check = False
            break
        if op[i] == '>' and num[i] < num[i + 1]:
            check = False
            break
    if check:
        print(''.join(map(str,num)))
        break

for num in pm(b,k+1):
    check = True
    for i in range(k):
        if op[i] == '<' and num[i] > num[i + 1]:
            check = False
            break
        if op[i] == '>' and num[i] < num[i + 1]:
            check = False
            break
    if check:
        print(''.join(map(str,num)))
        break
