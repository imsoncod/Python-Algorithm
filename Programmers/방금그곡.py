def solution(m, music):
    ans = []
    m=m.replace('C#', 'H')
    m=m.replace('D#', 'I')
    m=m.replace('F#', 'J')
    m=m.replace('G#', 'K')
    m=m.replace('A#', 'L')
    for i in music:
        temp = i.split(',')
        h1, m1 = temp[0].split(':')
        h2, m2 = temp[1].split(':')
        time = (int(h2)-int(h1))*60+int(m2)-int(m1)
        temp[3]=temp[3].replace('C#', 'H')
        temp[3]=temp[3].replace('D#', 'I')
        temp[3]=temp[3].replace('F#', 'J')
        temp[3]=temp[3].replace('G#', 'K')
        temp[3]=temp[3].replace('A#', 'L')
        temp[3] = (time//len(temp[3]))*temp[3] + temp[3][:time%len(temp[3])]
        if m in temp[3]:
            ans.append([temp[2],time,music.index(i)])
    if len(ans)>1:
        ans.sort(key=lambda x:(-x[1],x[2]))
    print(ans)
    return ans[0][0] if len(ans)!=0 else '(None)'
