# {1, 2, 3} 모든 부분 집합 출력하기
count = 0
N = 3
A = [0 for _ in range(N)]  # 원소의 포함여부 저장 (0, 1)
data = [1, 2, 3]


def printSet(n):
    global count
    count += 1
    print('%d : ' % (count), end='')  # 생성되는 부분 개열의 개수 출력
    for i in range(n):  # 각 부분 배열의 원소 출력
        if A[i] == 1:
            print('%d ' % data[i], end='')
    print()


def powerSet(n, k):
    if n == k:
        printSet(n)
    else:
        A[k] = 1
        powerSet(n, k + 1)
        A[k] = 0
        powerSet(n, k + 1)


powerSet(N, 0)
