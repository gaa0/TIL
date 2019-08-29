import sys
sys.stdin = open("view_input1.txt")
T = 10
for tc in range(1, T+1):
    N = int(input())   # 100
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(2, N-2):
        mh = 255
        for j in range(5):
            if j != 2:
                if arr[i] - arr[i-2+j] < mh:
                    mh = arr[i] - arr[i-2+j]
        if mh > 0:
            ans += mh

    print("#{} {}".format(tc, ans))
