n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)
team =- 0
#여자2명 + 남자1명 = 1팀
#여자가 2명 이상이고 남자가 1명이상 있을 때 인턴으로 빠질 수 있는 인원수만큼 남아있으면 3명으로 팀을 만든다 
while n >= 2 and m >= 1 and n+m - 3 >= k:
    n-=2
    m-=1
    team+=1

print(team)
