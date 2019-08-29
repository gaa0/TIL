def go(x, y):
    global flag
    if flag == 1:
        return
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    for i in range(4):
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N and data[x+dx[i]][y+dy[i]] != 1 and visited[x+dx[i]][y+dy[i]] == 0:
            a = x+dx[i]
            b = y+dy[i]
            if data[a][b] == 3:
                flag = 1
                return
            else:
                visited[a][b] = 1
                go(a, b)


import sys
sys.stdin = open('미로_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    data = []
    for _ in range(N):
        d = input()
        dd = []
        for i in d:
            dd.append(int(i))
        data.append(dd)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    flag = 0

    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                start = i, j
                visited[i][j] = 1

    go(start[0], start[1])

    print('#{} {}'.format(tc+1, flag))
