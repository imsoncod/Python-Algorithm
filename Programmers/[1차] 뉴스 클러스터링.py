def solution(str1, str2):
    str1,str2 = str1.lower(), str2.lower()
    a = []; b = []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            a.append(str1[i:i+2])
    for i in range(len(str2)-1): 
        if str2[i:i+2].isalpha():
            b.append(str2[i:i+2])
    its = 0;
    for s in a:
        if s in b:
            b.remove(s)
            its+=1
    print(a,b)        
    return (its/(len(a)+len(b))*65536)//1 if len(a)!=0 or len(b)!=0 else 65536
