import sys
sys.stdin = open('1_input.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    data = []
    for i in range(M):
        d = list(map(int, input().split()))
        data.append(d)

    s = [[0 for i in range(N)] for j in range(N)]

    for d in data:
        for i in range(d[0]-1, d[2]):
            for j in range(d[1]-1, d[3]):
                s[i][j] = 1

    ans = 0
    for ss in s:
        ans += sum(ss)

    print('#{} {}'.format(tc+1, ans))
