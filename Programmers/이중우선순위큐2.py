def solution(oper):
    h = []
    for i in oper:
        cmd = i.split(' ')
        if cmd[0]=='I':
            h.append(int(cmd[1]))
        else:
            try:
                if cmd[1]=='1':
                    h.remove(max(h))
                else:
                    h.remove(min(h))
            except:
                continue
    return [max(h), min(h)] if len(h)>0 else [0,0]
