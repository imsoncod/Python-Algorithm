import heapq as h
def solution(n, works):
    heap = []
    for i in works:
        h.heappush(heap, -i)
    for i in range(n):
        m=h.heappop(heap)
        m+=1
        if m!=0:
            h.heappush(heap, m)
        if not len(heap):
            break
    return sum([i**2 for i in heap]) if len(heap) else 0
