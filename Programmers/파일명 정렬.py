import re
def solution(files):
    temp = [re.split("([0-9]+)",s) for s in files]
    temp = sorted(temp, key=lambda x:(x[0].lower(),int(x[1])))
    return [''.join(s) for s in temp]
