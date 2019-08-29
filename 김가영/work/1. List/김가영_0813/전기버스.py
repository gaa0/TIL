import sys
sys.stdin = open("전기버스_input.txt")
T = int(input())
for tc in range(T):
    first = list(map(int, input().split()))
    K = first[0]
    N = first[1]
    M = first[2]
    data = list(map(int, input().split()))

    i = 0
    cnt = 0
    while i <= N:
        for j in range(i+K, i, -1):
            if j == N:
                break
            if j in data:
                cnt += 1
                i = j - 1
                break

        i += 1
    for i in range(len(data)):
        if i < len(data)-1:
            if data[i+1] - data[i] > K:
                cnt = 0

    print("#{} {}".format(tc+1, cnt))
