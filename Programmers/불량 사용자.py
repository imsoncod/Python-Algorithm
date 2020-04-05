import re
from itertools import permutations

def solution(user_id, banned_id):
    ans = []
    n = len(banned_id)
    for i in range(n):
        banned_id[i] = banned_id[i].replace('*','.')

    for array in list(permutations(user_id, n)):
        temp = []
        for user, ban in zip(array, banned_id):
            # ^ : 문자열의 시작 / $ : 문자열의 끝
            m = re.compile('^'+ban+'$') # 컴파일 패턴을 등록
            if m.match(user): # 문자열 매칭 확인
                temp.append(user)
        if len(temp) == n and sorted(temp) not in ans:
            ans.append(sorted(temp))
    return len(ans)
