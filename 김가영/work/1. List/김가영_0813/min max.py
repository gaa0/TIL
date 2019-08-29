import sys
sys.stdin = open("min max_input.txt")
T = int(input())  # type: int
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    mina = 1000000
    maxa = 0
    for i in data:
        if i < mina:
            mina = i
        if i > maxa:
            maxa = i


    print("#{} {}".format(tc, maxa - mina))
