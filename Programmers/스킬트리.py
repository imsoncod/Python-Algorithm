def solution(skill, tree):
    ans = len(tree)
    for t in tree:
        s = skill
        temp = ''
        for i in t:
            if i in skill:
                if i==s[0]:
                    temp += i
                    s = s[1:]
                else:
                    ans-=1
                    break
            else:
                temp+=i   
    return ans
