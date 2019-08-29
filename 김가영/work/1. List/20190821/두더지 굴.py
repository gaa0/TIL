import sys
sys.stdin = open('두더지 굴.txt')

T = int(input())
data = []
for i in range(T):
    d = list(map(int, input().split()))
    data.append(d)
    print(i, d)
visited = [[0 for _ in range(T)] for _ in range(T)]


def check(x, y):
    if x < 0 and y


def dfs(x, y):
    visited[x][y] = 1
    data[x][y] = 0



cnt = 0
for i in range(T):
    for j in range(T):
        if data[i][j] == 1:
            cnt += 1
            dfs(i, j)
