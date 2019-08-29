def bfs(v):
    q = []
    q.append(v)
    print(v, end=' ')
    visited[v] = 1
    while q:
        v = q.pop(0)
        for w in range(1, V+1):
            if G[v][w] == 1 and visited[w] == 0:
                q.append(w)
                print(w, end=' ')
                visited[w] = visited[v] + 1


import sys
sys.stdin = open('작업순서_input.txt')

T = 10

for tc in range(T):
    print('#{}'.format(tc + 1), end=' ')
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    s = set(data)
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for i in range(0, len(data), 2):
        G[data[i]][data[i+1]] = 1
    for i in s:
        chk = 0
        for j in s:
            if G[j][i] != 0:
                chk = 1
        if chk == 0:
            bfs(i)
    print()
