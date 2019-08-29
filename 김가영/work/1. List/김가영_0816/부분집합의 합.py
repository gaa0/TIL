import sys
sys.stdin = open("부분집합의 합_input.txt")

T = int(input())
for tc in range(T):
    data = list(map(int, input().split()))
    N = data[0]
    K = data[1]

    A = list(range(1, 13))

    n = len(A)

    bb = []
    for i in range(1<<n):
        b = []
        for j in range(n+1):
            if i & (1<<j):
                b.append(A[j])
        bb.append(b)

    cnt = 0
    for i in range(len(bb)):
        if len(bb[i]) == N and sum(bb[i]) == K:
            cnt += 1

    print('#{} {}'.format(tc+1, cnt))
