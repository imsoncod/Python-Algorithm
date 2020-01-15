def solution(n, words):
    temp = []
    words.insert(0,'')
    prev = words[1]
    temp.append(prev)
    for i in range(2,len(words)):
        if prev[-1] != words[i][0] or words[i] in temp:
            print(i,n)
            return [i%n, i//n+1] if i%n!=0 else [n, i//n]      
        prev = words[i]
        temp.append(prev)
    return [0, 0]
