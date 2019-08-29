def paper(N):
    n = N/10
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n%2 == 1:
        return paper(N-20) + 4**((n-1)/2)
    elif n%2 == 0:
        return paper(N-20) + 2*4**((n-2)/2)

import sys
sys.stdin = open('종이붙이기_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())

    print('#{} {}'.format(tc+1, int(paper(N))))
