def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        v = queue.pop(0)
        for w in range(1, N+1):
            if G[v][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[v] + 1


import sys
sys.stdin = open('Contact_input.txt')

T = 10
for tc in range(T):
    N, S = map(int, input().split())
    data = list(map(int, input().split()))
    G = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    for i in range(0, N, 2):
        G[data[i]][data[i+1]] = 1
    bfs(S)

    for idx, i in enumerate(visited):
        if i == max(visited):
            ans = idx

    print('#{} {}'.format(tc+1, ans))
