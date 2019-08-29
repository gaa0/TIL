def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    print(v, end=' ')
    while len(queue) != 0:
        v = queue.pop(0)
        for w in range(1, V+1):
            if G[v][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[v] + 1
                print(w, end=' ')


import sys
sys.stdin = open('연습3_input.txt')
V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for i in range(V+1)] for j in range(V+1)]
visited = [0 for _ in range(V+1)]
for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1
for i in range(V+1):
    print('{} {}'.format(i, G[i]))
bfs(1)

print()

for idx, i in enumerate(visited):
    if i == max(visited):
        print(idx, i-1)