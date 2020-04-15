# 내 코드
n, m = map(int, input().split())
dna = []
s = ""
hd = 0

for _ in range(n):
    dna.append(list(input()))

for i in range(m):
    nc = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for j in range(n):
        nc[dna[j][i]] += 1
    nc = sorted(nc.items(), key=lambda x: (-x[1],x[0])) #나온횟수가 동일할경우 알파벳순으로 정렬해주는게 포인트
    s += nc[0][0]
    hd += n - nc[0][1]

print(s)
print(hd)

#====================================================================================#

# 다른 사람 코드
N,M = map(int,input().split())
dna = []
result =''
hd = 0
for i in range(N):
    dna.append(input())

for i in range(M):
    cnt = [0,0,0,0] #알파벳순으로 더해주는게 포인트
    for j in range(N):
        if dna[j][i] == 'A':
            cnt[0] +=1
        elif dna[j][i] =='C':
            cnt[1] +=1
        elif dna[j][i] == 'G':
            cnt[2] +=1
        elif dna[j][i] == 'T':
            cnt[3] +=1

    Max = max(cnt)
    idx = cnt.index(Max)
    if idx ==0:
        result+='A'
    elif idx==1:
        result+='C'
    elif idx==2:
        result+='G'
    elif idx==3:
        result+='T'
    hd += N - Max

print(result)
print(hd)
