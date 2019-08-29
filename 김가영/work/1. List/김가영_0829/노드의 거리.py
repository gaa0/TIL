def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        v = queue.pop(0)
        for w in range(1, V+1):
            if gr[v][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[v] + 1



import sys
sys.stdin = open('노드의 거리_input.txt')

T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    gr = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for i in data:
        gr[i[0]][i[1]] = 1
        gr[i[1]][i[0]] = 1

    bfs(S)
    print(visited)

    ans = visited[G] - 1
    if ans == -1:
        ans = 0
    print('#{} {}'.format(tc+1, ans))