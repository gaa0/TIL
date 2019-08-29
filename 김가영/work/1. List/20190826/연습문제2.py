# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
count = 0
total = 0
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(data)
A = [0 for _ in range(N)]  # 원소의 포함여부 저장 (0, 1)


def printSet(n, sum):
    global count
    if sum == 10:
        count += 1
        print('%d : ' % count, end='')  # 생성되는 부분 개열의 개수 출력
        for i in range(n):
            if A[i] == 1:
                print("%d " % data[i], end='')
        print()


def powerSet(n, k, sum):
    global total

    if sum > 10:
        return

    total += 1
    if n == k:
        printSet(n, sum)
    else:
        A[k] = 1
        powerSet(n, k + 1, sum + data[k])
        A[k] = 0
        powerSet(n, k + 1, sum)


powerSet(N, 0, 0)
print('호출횟수 : {}'.format(total))
