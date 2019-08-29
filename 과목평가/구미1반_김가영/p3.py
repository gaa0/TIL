def check(data):
    s = 0
    for i in data:
        s += sum(i)
    if s != 0:
        global cnt
        cnt += 1
        count(data)
    else:
        return


def count(data):
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0 and visited[i][j] != 1:
                x = i
                y = j
                st.append([x, y])
                visited[x][y] = 1
                data[x][y] = 0
                island([x, y])


def island(xy):
    x = xy[0]
    y = xy[1]
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]  # 상~왼쪽위
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    for i in range(8):
        if 0 <= x+dx[i] and x+dx[i] < N and 0 <= y+dy[i] and y+dy[i] < N and data[x+dx[i]][y+dy[i]] != 0 and visited[x+dx[i]][y+dy[i]] != 1:
            x = x + dx[i]
            y = y + dy[i]
            st.append([x, y])
            visited[x][y] = 1
            data[x][y] = 0
            island([x, y])
    if st:
        island(st.pop())
    check(data)


import sys
sys.stdin = open('p3.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    data = []
    for n in range(N):
        d = list(map(int, input().split()))
        data.append(d)

    visited = [[0 for _ in range(N)] for _ in range(N)]
    st = []
    cnt = 0
    check(data)

    print('#{} {}'.format(tc+1, cnt))
