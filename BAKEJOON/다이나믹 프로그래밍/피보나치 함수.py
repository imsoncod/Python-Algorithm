#0과 1을 호출하는 횟수가 피보나추 수열을 이룬다
T = int(input())
for _ in range(T):
    n = int(input())
    zero = [1,0]
    one = [0,1]
    for i in range(2,n+1):
        zero.append(zero[i-1] + zero[i-2])
        one.append(one[i-1] + one[i-2])
    print(zero[n], one[n])
