def solution(cacheSize, cities):
    time = 0
    cache = []
    cities = [c.lower() for c in cities]
    if cacheSize!=0:
        for c in cities:
            if c in cache:
                cache.pop(cache.index(c))
                cache.append(c)
                time+=1
            else:
                if len(cache)<cacheSize:
                    cache.append(c)
                    time+=5
                else:
                    cache.pop(0)
                    cache.append(c)
                    time+=5
    else: 
        time += len(cities)*5               
    return time
