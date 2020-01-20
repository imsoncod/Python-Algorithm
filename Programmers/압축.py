def solution(msg):
    dic = [chr(i) for i in range(65,91)]
    ans = []
    c=' '
    while len(c)!=0:
        c=''
        for i in range(len(msg)-1,-1,-1):
            if msg[:i+1] in dic:
                w = msg[:i+1]
                ans.append(dic.index(w)+1)
                if i+1<len(msg):
                    c = msg[i+1]
                    dic.append(w+c)
                    msg = msg[i+1:]
                break
    return ans
