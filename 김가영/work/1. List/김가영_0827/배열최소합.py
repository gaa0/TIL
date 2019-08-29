def printArr(n):
    global sum
    global total
    a = 0
    for i in range(n):
        a += data[i][arr[i]]
        total += 1
        if a >= sum:
            return
    if a < sum:
        sum = a


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
    sum = 10 * N
    perm(N, 0)

    ans = sum
    print('#{} {}'.format(tc + 1, ans))
print(total)
