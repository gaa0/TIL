import sys
sys.stdin = open("dal_input.txt")

T = int(input())
for tc in range(T):
    print('#{}'.format(tc + 1))
    N = int(input())
    data = list(range(1, N**2+1))
    i = 0
    dd = []
    while i < N:
        d = []
        for j in range(0, N*N, N):
            d.append(0)
        dd.append(d)
        i += 1
    dx = [0, 1, 0, -1] # 우하좌상
    dy = [1, 0, -1, 0]
    dx = dx*N
    dy = dy*N

    x = 0
    y = 0
    idx = 0
    i = 1
    while i < N**2+1:
        if i == 1:
            dd[x][y] = '{}'.format(i)
            i += 1
        else:
            x = x + dx[idx]
            y = y + dy[idx]
            if x >= N or y >= N or dd[x][y] != 0:
                x = x - dx[idx]
                y = y - dy[idx]
                idx += 1
                x = x + dx[idx]
                y = y + dy[idx]
                dd[x][y] = '{}'.format(i)
                i+=1
            else:
                dd[x][y] = '{}'.format(i)
                i += 1
    for i in range(N):
        print(' '.join(dd[i]))
