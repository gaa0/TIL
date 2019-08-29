import sys
sys.stdin = open("숫자 카드_input.txt")
T = int(input())
for tc in range(T):
    N = int(input())
    data = input()

    count = [0]*10

    for i in data:
        count[int(i)] += 1

    many = 0
    for i in range(len(count)):
        if count[i] > many:
            many = count[i]
            max_num = i

    big = 0
    for idx, val in enumerate(count):
        if count[max_num] == count[idx]:
            big = idx

    print("#{} {} {}".format(tc+1, big, many))
