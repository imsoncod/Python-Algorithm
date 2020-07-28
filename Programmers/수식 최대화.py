# 우선순위가 - > * > + 일 경우
# -를 계산하기 위해서는 *의 계산값이 필요하고 *를 계산하기 위해서는 +의 계산값이 필요하다
# 때문에 재귀 + 분할정복으로 탐색한다

def calc(case, n, expression):
    if n == 2:
        return str(eval(expression))
    if case[n] == '*':
        res = '*'.join([calc(case, n+1, e) for e in expression.split('*')])
    elif case[n] == '+':
        res = '+'.join([calc(case, n+1, e) for e in expression.split('+')])
    elif case[n] == '-':
        res = '-'.join([calc(case, n+1, e) for e in expression.split('-')])
    return str(eval(res))

def solution(expression):
    answer = 0
    cases = [
        ('*', '+', '-'),
        ('*', '-', '+'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('-', '*', '+'),
        ('-', '+', '*')
    ]

    for case in cases:
        res = int(calc(case, 0, expression))
        answer = max(answer, abs(res))

    return answer
