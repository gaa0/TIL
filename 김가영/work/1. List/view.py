import sys
sys.stdin = open("view_input1.txt")
T = 10
for tc in range(1, T+1):
    N = int(input())   # 100
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(2, len(arr)-1):
        if arr[i-2] < arr[i] and arr[i-1] < arr[i] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            if arr[i-2] > arr[i-1]:
                left = arr[i] - arr[i-2]
            if arr[i-2] <= arr[i-1]:
                left = arr[i] - arr[i-1]
            if arr[i+2] > arr[i+1]:
                right = arr[i] - arr[i+2]
            if arr[i+2] <= arr[i+1]:
                right = arr[i] - arr[i+1]
            if left > right:
                ans += right
            if left <= right:
                ans += left




    print("#{} {}".format(tc, ans))