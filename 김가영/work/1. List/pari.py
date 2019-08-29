import sys
sys.stdin = open("pari_input.txt")

T = int(input())
for tc in range(T):
    a = list(map(int, input().split()))
    N = a[0]
    M = a[1]
    data = []
    for i in range(N):
        d = list(map(int, input().split()))
        data.append(d)

    mari = 2*M**2
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for k in range(M):
                s += sum(data[i+k][j:j+M])
            if s > mari:
                mari = s

    print('#{} {}'.format(tc+1, mari))
