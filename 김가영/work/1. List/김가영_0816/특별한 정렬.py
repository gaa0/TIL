import sys
sys.stdin = open("특별한 정렬_input.txt")

T = int(input())


def selectionSort(a):
    for i in range(0, len(a)-1):
        max = i
        min = i
        if i%2 == 0:
            for j in range(i+1, len(a)):
                if int(a[max]) < int(a[j]):
                    max = j
            a[i], a[max] = a[max], a[i]
        if i%2 == 1:
            for j in range(i+1, len(a)):
                if int(a[min]) > int(a[j]):
                    min = j
            a[i], a[min] = a[min], a[i]

for tc in range(T):
    N = int(input())
    data = list(map(str, input().split()))
    selectionSort(data)
    d = data[0:10]
    ans = ' '.join(d)
    print('#{} {}'.format(tc+1, ans))