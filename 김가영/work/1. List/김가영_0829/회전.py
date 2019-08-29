import sys
sys.stdin = open('회전_input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    for i in range(M):
        data.append(data.pop(0))

    ans = data[0]
    print('#{} {}'.format(tc+1, ans))
