def base(num,n):
    if num==0:
        return '0'
    temp = []
    alpha = 'ABCDEF'
    while num!=0:
        num,r = divmod(num,n)
        if r >= 10:
            r = alpha[r%10]
        temp.insert(0,str(r))
    return ''.join(temp)

def solution(n,t,m,p):
    ans = ''
    num = 0
    while len(ans)<t*m:
        ans += base(num,n)
        num+=1
    return ''.join([ans[i] for i in range(p-1,t*m,m)])
