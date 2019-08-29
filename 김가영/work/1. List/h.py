import sys
sys.stdin = open("h_input.txt")

for tc in range(10):
    N = int(input())
    data = []
    for i in range(8):
        d = input()
        data.append(list(d))

    data2 = []
    for i in range(8):
        dd = []
        for j in range(8):
            dd.append(data[j][i])
        data2.append(dd)

    cnt = 0
    for i in range(8):
        for j in range(9-N):
            a = data[i][j:j+N]
            if a == a[::-1]:
                cnt += 1
    for i in range(8):
        for j in range(9-N):
            a = data2[i][j:j+N]
            if a == a[::-1]:
                cnt += 1

    print('#{} {}'.format(tc+1, cnt))