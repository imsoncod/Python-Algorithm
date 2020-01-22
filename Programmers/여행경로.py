answer = []

def dfs(tickets, start, ans):
    b = [a for a in ans]
    b.append(start)
    for i in tickets:
        temp = [t for t in tickets]
        if i[0] == start:
            temp.remove(i)
            dfs(temp, i[1], b)
    if len(tickets)==0:
        global answer
        if len(answer)<len(b):
            answer = [i for i in b]
def solution(tickets):
    tickets = sorted(tickets, key=lambda x:(x[0],x[1]))
    global answer
    dfs(tickets,'ICN',[])
    return answer
