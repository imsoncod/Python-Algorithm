m = 1000 - int(input())
coin = [500,100,50,10,5,1]
ans = 0
for c in coin:
    ans += m//c
    m = m%c
print(ans)
