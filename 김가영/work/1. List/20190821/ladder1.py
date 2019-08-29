import sys
sys.stdin = open('ladder1_sample_input.txt')

for tc in range(1):  # 10
    print('#{}'.format(int(input())), end=' ')
    data =[]
    for i in range(10):  # 100
        d = list(map(int, input().split()))
        data.append(d)
    visited = [[0 for _ in range(10)] for _ in range(10)]  # 100

    for i in range(10):  # 100
        if data[9][i] == 2:  # data[99][i]
            start = i

    upx = -1
    dy = [-1, 1]
    dy = dy*100

    x = 9  # 99
    y = start
    idx = 0
    s = 0
    while s < 100:  # 10000
        if s == 0:
            visited[x][y] = 1
            x = x - 1

        if x < 0:
            x = x + 1
            print(y)
            break
        cnt = 0
        for i in range(2):
            y = y + dy[i]
            if y >= 10 or data[x][y] != 1:  # 100
                y = y - dy[i]
                cnt += 1

        if cnt == 2:
            x = x - 1
            data[x][y] = 1

        cnt = 0
        for i in range(20):  # 200
            y = y + dy[i]
            if y < 10 and data[x][y] == 1:
                if visited[x][y] == 0:
                    visited[x][y] = 1
                if visited[x][y] == 1:
                    y = y - dy[i]
            if y >= 10 or data[x][y] == 0:
                y = y - dy[i]
                cnt += 1
            if cnt == 2:
                break

        s += 1