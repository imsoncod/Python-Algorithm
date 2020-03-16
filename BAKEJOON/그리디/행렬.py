#좌측 상단부터 그리디하게 비교
#(i,j)의 값이 다를때만 뒤집어주고 이미 뒤집은 값은 다시 볼 필요가 없다
import copy
n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    a.append(list(input()))
for _ in range(n):
    b.append(list(input()))

#깊은 복사
c = copy.deepcopy(a)
ans = 0

for i in range(n-2):
    for j in range(m-2):
        if c[i][j] != b[i][j]:
            for p in range(i,i+3):
                for q in range(j,j+3):
                    c[p][q] = '0' if c[p][q]=='1' else '1'
            ans += 1

ans = ans if b==c else -1
print(ans)
