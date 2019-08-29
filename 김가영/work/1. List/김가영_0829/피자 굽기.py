def isFull():
    global front, rear
    return (rear+1) % len(Q) == front


def isEmpty():
    global front, rear
    return front == rear


def enQueue(item):
    global rear
    if isFull():
        return
    else:
        rear = (rear+1) % len(Q)
        if item == 0:
            Q[rear] = 0
        else:
            Q[rear] = [item[0], item[1]]
            C.pop(0)


def deQueue():
    global front
    if isEmpty():
        return 'Queue_Empty'
    else:
        front = (front+1)%len(Q)
        if Q[front] == 0:
            if front == len(Q) - 1:
                front = 0
            return
        elif Q[front][1] > 0:
            Q[front][1] = Q[front][1]//2
            if Q[front][1]//2 == 0 and C:
                Q[front] = C.pop(0)
            elif Q[front][1]//2 == 0 and len(C) == 0:
                Q[front] = 0
            if front == len(Q) - 1:
                front = 0


import sys
sys.stdin = open('피자 굽기_input.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    C = [[idx+1, i] for idx, i in enumerate(Ci)]

    SIZE = N + 1
    Q = [0]*SIZE
    front, rear = 0, 0

    while Q.count(0) != 1:
        enQueue(C[0])

    while Q.count(0) != N:
        deQueue()


    for i in Q:
        if i != 0:
            ans = i[0]
    print('#{} {}'.format(tc+1, ans))
