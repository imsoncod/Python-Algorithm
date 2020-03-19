n, l = map(int, input().split())
p = sorted(list(map(int, input().split())))

tape = 1
idx = 0

for i in range(n):
    #idx를 시작으로 테이프를 붙여 최대 수용 범위를 구함
    temp = p[idx]+l-1
    
    #이미 테이프를 붙일 수 있는 범위 내에 있을 경우
    if p[i] <= temp:
        continue    
    else:
        tape += 1
        idx = i
print(tape)
