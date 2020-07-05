#스택의 기본 문제
n, k = map(int, input().split())
temp = k
num = input()
stack = []

for i in num:
    while k > 0 and stack and stack[-1] < i: #stack[-1] 조건을 앞에 써주면 index에러가 발생한다
        stack.pop(-1)
        k -= 1
    stack.append(i)

print(''.join(stack[:n-temp]))
