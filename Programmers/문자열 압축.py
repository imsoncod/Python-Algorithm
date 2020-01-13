def solution(s):
    answer = 1000
    for i in range(1,(len(s)//2)+1):
        arr = [s[j:j+i] for j in range(0,len(s),i)]
        a=1; x=''; b=[]
        temp = ''
        while len(arr)!=0:
            x=arr.pop(0)
            for j in range(0,len(arr)):
                if x==arr[0] and len(arr[0])==i:
                    del arr[0]
                    a+=1
                else :
                    temp += (x if a==1 else str(a)+x)
                    a=1
                    break
        temp += (x if a==1 else str(a)+x)
        answer = min(answer,len(temp))
    return answer if len(s)!=1 else 1
