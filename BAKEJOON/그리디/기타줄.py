n, m = input().split()
n = int(n)
m = int(m)
a = []
b = []

for _ in range(m):
    p1, p2 = input().split()
    p1 = int(p1)
    p2 = int(p2)
    #사기적으로 패키지가격이 낱개로사는것보다 비쌀경우 -> 패키지로 구매할 필요가 없다..
    if p1 > p2*6:
        p1 = p2*6
    a.append(p1)
    b.append(p2)

#가장 저렴한 패키지값*필요한 패키지갯수 + min(남는낱개를 패키지로살경우 or 낱개로 살경우)
ans = min(a)*(n//6) + min(min(a), min(b)*(n%6))
print(ans)
