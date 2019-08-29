import sys
sys.stdin = open("이진탐색_input.txt")

T = int(input())


def binarySearch(a, key):
    start = 1
    end = a
    cnt = 0
    while start <= end:
        cnt += 1
        middle = (start + end)//2
        if middle == key:
            return cnt
        elif middle > key:
            end = middle
        else:
            start = middle
    return False


for tc in range(T):
    data = list(map(int, input().split()))
    P = data[0]
    Pa = data[1]
    Pb = data[2]
    aa = binarySearch(P, Pa)
    bb = binarySearch(P, Pb)
    if aa < bb:
        ans = 'A'
    elif aa > bb:
        ans = 'B'
    else:
        ans = 0
    print('#{} {}'.format(tc+1, ans))
