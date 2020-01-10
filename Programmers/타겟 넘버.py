answer = 0
def solution(numbers, target):
    search(numbers, target, 0, 0)
    return answer

def search(numbers, target, result, idx):
    global answer
    if idx==len(numbers):
        if target==result:
            answer+=1
            return
        return
    search(numbers,target,result+numbers[idx],idx+1)
    search(numbers,target,result-numbers[idx],idx+1)
