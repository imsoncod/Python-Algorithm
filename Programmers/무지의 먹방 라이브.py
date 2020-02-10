from queue import PriorityQueue
def solution(foods, k):
    if sum(foods) <= k:
        return -1
    q = PriorityQueue()
    for i in range(len(foods)):
        q.put((foods[i],i+1))
    prev = 0
    now = 0
    temp = 0
    length = len(foods)
    while temp + (q.queue[0][0]-prev)*length <= k:
        now = q.get()[0]
        temp += (now-prev)*length
        length-=1
        prev = now
    target = k - temp
    result = sorted(q.queue, key=lambda x:x[1])
    target = target%len(result) + 1
    return result[target-1][1]
