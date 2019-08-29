import sys
sys.stdin = open("sum_input.txt")

T = 10
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    b = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += data[i][j]
        if sum > b:
            b = sum
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += data[j][i]
        if sum > b:
            b = sum
    for i in range(100):
        sum = 0
        sum += data[i][i]
        if sum > b:
            b = sum
    for i in range(100):
        sum = 0
        sum += data[i][99-i]
        if sum > b:
            b = sum

    print('#{} {}'.format(tc+1, b))
