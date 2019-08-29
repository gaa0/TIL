import sys

sys.stdin = open('사각형 칠하기_input.txt')

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    data = [[int(num) for num in input().split()] for _ in range(K)]

    b = [[0 for _ in range(M)] for _ in range(N)]
    s = {0}
    for i in range(K):
        s.add(data[i][4])

    for i in range(K):
        if i == 0:
            for j in range(data[0][0], data[0][2] + 1):
                for k in range(data[0][1], data[0][3] + 1):
                    b[j][k] = data[0][4]
        else:
            chk = 0
            for j in range(data[i][0], data[i][2] + 1):
                for k in range(data[i][1], data[i][3] + 1):
                    if b[j][k] > data[i][4]:
                        chk = 1
                        break
                if chk == 1:
                    break
            if chk == 0:
                for j in range(data[i][0], data[i][2] + 1):
                    for k in range(data[i][1], data[i][3] + 1):
                        b[j][k] = data[i][4]

    ss = 0
    for i in s:
        sss = 0
        for j in range(N):
            sss += b[j].count(i)
        if sss > ss:
            ss = sss

    print('#{} {}'.format(tc + 1, ss))
