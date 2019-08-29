def start_check(v):
    for d in data:
        if visited[d[0]][d[1]] != 1:
            if v[0] == d[0]:
                start(v)
            else:
                visited[d[0]][d[1]] = 1
                start_check(v)
    return 0


def start(v):
    for d in data:
        if v[0] == d[0]:
            if d[1] == chk[1]:
                return 1
            else:
                go(d)


def go(v):
    for d in data:
        if v[1] == d[0]:
            if d[1] == chk[1]:
                global c
                c = 1
                return 1
            else:
                go(d)
    return 0


import sys
sys.stdin = open('그래프경로_input.txt')

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    data = []
    for i in range(E):
        d = list(map(int, input().split()))
        data.append(d)

    chk = list(map(int, input().split()))

    ss = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for i in data:
        ss[i[0]][i[1]] = 1

    c = 0
    start_check(chk)

    print('#{} {}'.format(tc+1, c))
