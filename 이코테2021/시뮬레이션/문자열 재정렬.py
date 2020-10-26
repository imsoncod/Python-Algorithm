def solution(data):
    alpha = []
    sum = 0

    for i in data:
        try:
            d = int(i)
            sum += d
        except:
            alpha.append(i)

    alpha = ''.join(sorted(alpha))
    sum = str(sum)

    return alpha + sum

print(solution("K1KA5CB7"))
print(solution("AJKDLSI412K4JSJ9D"))
