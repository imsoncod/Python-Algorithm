import re
def solution(word, pages):
    sites = []
    my_score = []
    default_score = []
    external_score = []
    external_link = []
    for p in pages:
        sites.append(re.search('<meta.+?content="(.+?)"',p).group(1))
        default_score.append(((re.sub('[^a-z]+','.',p.lower())).split('.').count(word.lower())))
        external_link.append(re.findall('<a href="(.+?)">', p))
        external_score.append(len(re.findall('<a href="(.+?)">', p)))
    for i in range(len(sites)):
        if external_score[i]==0:
            my_score.append(0)
            continue
        my_score.append(default_score[i]/external_score[i])
    for i in range(len(sites)):
        s = 0
        for j in external_link[i]:
            if j in sites:
                goal = sites.index(j)
                default_score[goal]+=my_score[i]
    return default_score.index(max(default_score))
