def solution(record):
    db={}
    ans = []
    for r in record:
        temp = r.split(' ')
        if len(temp) > 2:
            db[temp[1]] = temp[2]    
    for r in record:
        temp = r.split(' ')
        if 'Leave' in temp:
            ans.append(db[temp[1]]+'님이 나갔습니다.')
        elif 'Enter' in temp:
            ans.append(db[temp[1]]+'님이 들어왔습니다.')
        else:
            continue    
    return ans
