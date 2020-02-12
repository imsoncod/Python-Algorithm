#startswith와 endswith
#효율성테스트 1,2,3 실패
def solution(words, queries):
    ans = []
    for ly in queries:
        length = len(ly)
        temp = 0
        if ly[-1] == '?':
            a = ly.split('?')[0]
            for w in words:
                if w.startswith(a) and length==len(w):
                    temp+=1
        elif ly[0] == '?':
            a = ly[::-1].split('?')[0][::-1]
            for w in words:
                if w.endswith(a) and length == len(w):
                    temp += 1
        ans.append(temp)
    return ans
