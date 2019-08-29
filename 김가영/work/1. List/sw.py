def printArr(n):
    ll = []
    for i in range(n):
        ll.append(arr[i])
    l.append(ll)


def perm(n, k):
    if k == n:
        printArr(n)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k + 1)
            arr[k], arr[i] = arr[i], arr[k]

import sys

sys.stdin = open('배열최소합_input.txt')

T = int(input())
total = 0
for tc in range(T):
    N = int(input())
    data = []
    for i in range(N):
        d = list(map(int, input().split()))
        data.append(d)

    arr = [i for i in range(N)]
    l = []
    perm(N, 0, 0)

    sum = 10 * N
    for i in l:
        chk = 0
        if chk == 0:
            a = 0
            for j in range(N):
                a += data[j][i[j]]
                total += 1
                if a >= sum:
                    chk = 1
                    break
            if a < sum:
                sum = a

    ans = sum
    print('#{} {}'.format(tc + 1, ans))
print(total)
