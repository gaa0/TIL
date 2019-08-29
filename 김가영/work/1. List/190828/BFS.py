def BFS(G,v):  # 그래프 G, 탐색 시작점 v
    queue = []  # 큐 생성
    queue.append(v)  # 시작점 v를 큐에 삽입
    visited[v] = 1
    while queue:  # 큐가 비어있지 않은 경우
        t = queue.pop(0)  # 큐의 첫 번째 원소 반환
        for i in range(1, n+1):  # t와 연결된 모든 선에 대해
            if G[t][i] and not visited[i]:  # 방문되지 않은 곳이라면
                queue.append(i)  # 큐에 넣기
                visited[i] = 1
                print(i)


n = 7
data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
dd = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0]*(n+1)  # n : 정점의 개수

for i in range(0, len(data), 2):
    dd[data[i]][data[i+1]] = 1
    dd[data[i+1]][data[i]] = 1
print(dd)
