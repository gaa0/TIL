import sys
sys.stdin = open("nasa_input.txt")

T = int(input())

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    dd = []
    for i in range(N):
        d = []
        for j in range(2):
            d.append(data[2*i+j])
        dd.append(d)

    su = []
    for i in range(N):
        su.append(dd[i][0])
    print(su)

    am = []
    for i in range(N):
        am.append(dd[i][1])
    print(am)

    for i in su:
        if i in am:
            su.remove(i)
    print(su)

    # min = 100
    # for i in range(len(dd)):
    #     if dd[i][0] < min:
    #         min = dd[i][0]

    # ans = []
    # for i in dd:
    #     if i[0] == min:
    #         ans.append(i)
    #         dd.remove(i)
    #         break
    #
    # for i in range(N-1):
    #     for j in range(len(dd)):
    #         if ans[i][1] == dd[j][0]:
    #             ans.append(dd[j])
    #             break
    #
    # print(ans)

    # print('#{} {}'.format(tc+1, 0))