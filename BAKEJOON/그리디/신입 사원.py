#자신보다 서류,면접 점수가 둘 다 높은 사람이 있으면 뽑힐 수 없다
#s[n] : 서류점수 n등의 면접점수
import sys
input = sys.stdin.readline
#input 여러줄 입력 속도를 높이기 위해 sys를 사용하도록 하자
T = int(input())
for _ in range(T):
    n = int(input())
    s = [0]*(n+1)
    for _ in range(n):
        a, b = map(int, input().split())
        s[a] = b

    ans = 1
    temp = s[1]
    for i in range(2, n+1):
        if temp > s[i]:
            temp = s[i]
            ans += 1
            if temp == 1:
                break
    print(ans)
