#올바른 괄호인지 판별
def isright(u):
    if u=='':
        return True
    temp = 0
    for i in u:
        if i =='(':
            temp+=1
        else:
            temp-=1
        if temp<0:
            return False
    return True
#u,v로 문자열 분배
def split(v):
    if v=='':
        return ''
    u=''
    cnt=0
    for i in v:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        u += i
        if cnt == 0:
            break
    v = v[len(u):]
    return u, v

def test(p):
    try:
        u,v = split(p)
    except:
        return ''
    ans=''
    if isright(u):
        ans+=u
        ans+=test(v)
        return ans
    else:
        ans+='('
        ans+=test(v)
        ans+=')'
        u=list(u[1:-1])
        for i in range(len(u)):
            u[i] = ')' if u[i] == '(' else '('
        u = ''.join(u)
        ans+=u
        return ans

def solution(p):
    ans = test(p)
    return ans
