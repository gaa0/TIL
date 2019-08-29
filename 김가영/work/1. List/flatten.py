import sys
sys.stdin = open("flatten_input.txt")
T = 10
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    d = {}
    for idx, val in enumerate(data):
        d[idx] = val



    for k in range(N):
        mina = 100
        maxa = 1
        for i in d.keys():
            if d[i] < mina:
                mina = d[i]
                mind = i
            if d[i] > maxa:
                maxa = d[i]
                maxd = i
        d[maxd] -= 1
        d[mind] += 1

    final_max = 1
    final_min = 100
    for i in d.keys():
        if d[i] < final_min:
            final_min = d[i]
        if d[i] > final_max:
            final_max = d[i]

    print('#{} {}'.format(tc+1, final_max - final_min))
