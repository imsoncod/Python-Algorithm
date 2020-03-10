n = list(input())
if '0' not in n:
    print(-1)
else:
    #30의 배수가 되려면 모든자리 수의 합이 3의배수 / 일의자리가 0
    if sum(list(map(int,n)))%3==0:
        print(''.join(sorted(n, reverse=True)))
    else:
        print(-1)
