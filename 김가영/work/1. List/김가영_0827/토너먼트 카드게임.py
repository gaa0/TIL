def K(t):
    if len(t) == 2:
        return rsp(t[0], t[1])
    elif len(t) == 3:
        newt1 = rsp(t[0], t[1])
        newt2 = t[2]
        return K([newt1, newt2])
    elif len(t)%2 == 0:
        newt1 = K(t[0:len(t)//2])
        newt2 = K(t[len(t)//2:len(t)])
        return K([newt1, newt2])
    else:
        newt1 = K(t[0:len(t)//2+1])
        newt2 = K(t[len(t)//2+1:len(t)])
        return K([newt1, newt2])


def rsp(a, b):
    if (a[1] == 1 and b[1] == 2) or (a[1] == 2 and b[1] == 3) or (a[1] == 3 and b[1] == 1):
        return b
    else:
        return a


import sys
sys.stdin = open('토너먼트 카드게임_input.txt')
T = int(input())

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    idx = [i+1 for i in range(N)]
    t = list(zip(idx, data))

    print('#{} {}'.format(tc+1, K(t)[0]))
