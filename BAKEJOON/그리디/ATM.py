n = int(input())

#걸리는 시간
#a b c d e
#a
#a+b
#a+b+c
#a+b+c+d
#a+b+c+d+e
#5a+4b+3c+2d+e
#na+(n-1)b+(n-2)c+(n-3)d+(n-4)e

arr = sorted(list(map(int, input().split())))
ans = 0

for i in range(n):
    ans += sum(arr[:i+1])

print(ans)
