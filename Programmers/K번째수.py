def solution(array, commands):
    answer = []
    for a in range(len(commands)):
        i,j,k = commands[a]
        array1 = array[i-1:j]
        array1.sort()
        answer.append(array1[k-1])
    return answer
