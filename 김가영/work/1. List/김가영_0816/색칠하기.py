import sys
sys.stdin = open("색칠하기 _input.txt")
T = int(input())
for tc in range(T):
    N = int(input())
    dd = []
    for i in range(N):
        data = list(map(int, input().split()))
        dd.append(data)

    gg = []
    for i in range(10):
        g = []
        for j in range(10):
            g.append(0)
        gg.append(g)

    for k in range(N):
        for i in range(dd[k][0], dd[k][2]+1):
            for j in range(dd[k][1], dd[k][3]+1):
                gg[i][j] += dd[k][4]

    cnt = 0
    for i in range(10):
        if 3 in gg[i]:
            cnt+=gg[i].count(3)

    print('#{} {}'.format(tc+1, cnt))