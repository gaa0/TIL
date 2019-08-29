import sys
sys.stdin = open("구간합.txt")
T = int(input())
for tc in range(T):
    N = list(map(int, input().split()))
    data = list(map(int, input().split()))

    mins = 0
    for i in range(N[0]):
        mins += data[i]

    maxs = 3

    for i in range(N[0]-N[1]+1):
        s = 0
        for j in range(N[1]):
            s += data[i+j]
        if s < mins:
            mins = s
        if s > maxs:
            maxs = s

    print("#{} {}".format(tc+1, maxs-mins))
