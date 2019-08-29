def start(xy):
    x = xy[0]
    y = xy[1]
    dx = [0, 1, 0, -1]  # 우하좌상
    dy = [1, 0, -1, 0]
    for i in range(4):
        if 0 <= x+dx[i] and x+dx[i] < 16 and 0 <= y+dy[i] and y+dy[i] < 16 and data[x+dx[i]][y+dy[i]] != 1 and visited[x+dx[i]][y+dy[i]] != 1:
            x = x + dx[i]
            y = y + dy[i]
            if x == end[0] and y == end[1]:
                global ans
                ans = 1
                return 1
            st.append([x, y])
            visited[x][y] = 1
            data[x][y] = 0
            start([x, y])
    if st:
        start(st.pop())
    else:
        return 0



import sys
sys.stdin = open('미로1_input.txt')

T = 10

for tc in range(T):
    N = int(input())
    data = []
    for i in range(16):
        d = input()
        dd = []
        for j in d:
            dd.append(int(j))
        data.append(dd)
    visited = [[0 for _ in range(16)] for _ in range(16)]
    st = []

    for i in range(16):
        for j in range(16):
            if data[i][j] == 2:
                x = i
                y = j
                visited[x][y] = 1
                data[x][y] = 0
                st.append([x, y])

    for i in range(16):
        for j in range(16):
            if data[i][j] == 3:
                end = [i, j]

    ans = 0
    start([x, y])

    print('#{} {}'.format(tc+1, ans))
