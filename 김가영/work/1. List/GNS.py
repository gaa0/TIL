import sys
sys.stdin = open("GNS_test_input.txt")

T = int(input())
for tc in range(T):
    sl = list(map(str, input().split()))
    tcn = sl[0]
    tl = sl[1]
    data = list(map(str, input().split()))
    sun = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    d = {}
    for i in range(int(tl)):
        d.update({data[i]: 0})

    for i in data:
        if i in d:
            d[i] += 1

    print(tcn)
    for i in range(len(sun)):
        for _ in range(d[sun[i]]):
            print(sun[i], end=' ')
    print()
