def solution(n, k):
    answer = 0
    while n >= k:
        temp = n%k # 1을 빼는 연산
        n //= k # k로 나누는 연산
        answer += temp + 1 # 1을 빼는 연산 + k로 나누는 연산

    answer += (n-1) # n < k 이므로 1을 빼는 연산만으로 추가 수행 
    return answer

print(solution(25, 3))
print(solution(17, 4))
