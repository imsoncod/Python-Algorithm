def solution(p):
    for data in p: #비교할 데이터를 꺼냄
        for idx in range(len(p)): 
            if p[idx] == data: continue #자기자신을 제외한 전부와 비교
            elif data in p[idx]: #자기자신이 아니고 비교대상에 포함되어 있으면
                if len(data) < len(p[idx]):
                    if p[idx].startswith(data): #접두어가 맞는지 확인
                        return False
    return True
