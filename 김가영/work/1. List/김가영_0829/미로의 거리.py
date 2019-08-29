def bfs(t):
    queue = []
    queue.append(t)
    x = t[0]
    y = t[1]
    visited[x][y] = 1
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    while queue:
        t = queue.pop(0)
        x = t[0]
        y = t[1]
        for i in range(4):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N and dd[x+dx[i]][y+dy[i]] != 1 and visited[x+dx[i]][y+dy[i]] == 0:
                a = x+dx[i]
                b = y+dy[i]
                if dd[a][b] == 3:
                    return visited[x][y] - 1
                queue.append((a, b))
                visited[a][b] = visited[x][y] + 1
    return 0


import sys
sys.stdin = open('미로의 거리_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    dd = []
    for i in range(N):
        data = input()
        d = []
        for j in data:
            d.append(int(j))
        dd.append(d)
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if dd[i][j] == 2:
                ans = bfs((i, j))
                break

    print('#{} {}'.format(tc+1, ans))
