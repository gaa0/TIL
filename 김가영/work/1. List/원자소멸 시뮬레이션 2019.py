import sys
sys.stdin = open('원자소멸 시뮬레이션 2019_input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    only = []
    for i in data:
        only.append([[i[0], i[1]], i[2], i[3]])

    ans = 0

    i = 0
    while i <= 4000:
        if only:
            for j in only:
                if j[1] == 0:
                    j[0][1] += 0.5
                elif j[1] == 1:
                    j[0][1] -= 0.5
                elif j[1] == 2:
                    j[0][0] -= 0.5
                elif j[1] == 3:
                    j[0][0] += 0.5
        for j in only:
            a = j[0]
            cnt = 0
            for k in only:
                if a in k:
                    cnt += 1
            if cnt >= 2:
                for k in only:
                    if a in k:
                        ans += k[2]
                        only.remove(k)
        i += 1

    # ii = 0
    # while ii <= len(only):
    #     if only:
    #         for j in only:
    #             chk = 0
    #             if j[1] == 0:
    #                 for k in only:
    #                     if k[1] == 1 and k[0][0] == j[0][0] and k[0][1] < j[0][1]:
    #                         chk = 1
    #                         ans += k[2]
    #                         only.remove(k)
    #                         break
    #             if chk == 1:
    #                 continue
    #             chk = 0
    #             if j[1] == 3:
    #                 for k in only:
    #                     if k[1] == 2 and k[0][1] == j[0][1] and k[0][0] < j[0][0]:
    #                         chk = 1
    #                         ans += k[2]
    #                         only.remove(k)
    #                         break
    #             if chk == 1:
    #                 continue
    #
    #     ii += 1

    print(only)


    print('#{} {}'.format(tc+1, ans))
