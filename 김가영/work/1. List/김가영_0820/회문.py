import sys
sys.stdin = open("회문_input.txt")

T = int(input())
for tc in range(T):
    nm = list(map(int, input().split()))
    N = nm[0]
    M = nm[1]
    data = []
    for i in range(N):
        d = input()
        data.append(list(d))

    data2 = []
    for i in range(N):
        dd = []
        for j in range(N):
            dd.append(data[j][i])
        data2.append(dd)

    ans = 0
    for i in range(N):
        for j in range(N+1-M):
            a = data[i][j:j+M]
            b = data2[i][j:j+M]
            if a == a[::-1]:
                ans = a
                break
            if b == b[::-1]:
                ans = b
                break
        if ans != 0:
            break

    print('#{} {}'.format(tc+1, ''.join(ans)))
