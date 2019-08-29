s = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
V, E = 7, 8
ss = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for i in range(V+1)]


def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(V+1):
        if ss[v][i] == 1 and visited[i] == 0:
            dfs(i)


for i in range(0, len(s), 2):
    ss[s[i]][s[i+1]] = 1
    ss[s[i+1]][s[i]] = 1

for i in range(V+1):
    print(i, ss[i])
dfs(1)
