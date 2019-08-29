import sys
sys.stdin = open('p2.txt')

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    data = []
    for i in range(N):
        d = list(map(int, input().split()))
        data.append(d)

    bigsize = []
    smallsize = []
    for i in range((N-(K-1))*(M-(K-1))):
        for n in range(N-(K-1)):
            for m in range(M-(K-1)):
                big = 0
                small = 0
                for nk in range(K):
                    for mk in range(K):
                        big += data[n+nk][m+mk]
                for snk in range(K-2):
                    for smk in range(K-2):
                        small += data[n+1+snk][m+1+smk]
                bigsize.append(big)
                smallsize.append(small)

    ans = []
    for i in range(len(bigsize)):
        a = bigsize[i] - smallsize[i]
        ans.append(a)

    print('#{} {}'.format(tc+1, max(ans)))
