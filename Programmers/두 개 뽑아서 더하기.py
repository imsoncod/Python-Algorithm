def solution(numbers):
    answer = []
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            sum = numbers[i]+numbers[j]
            if sum not in answer:
                answer.append(sum)

    return sorted(answer)
