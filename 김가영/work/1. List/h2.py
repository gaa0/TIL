import sys
sys.stdin = open("h2_input.txt")

for tc in range(10):
    N = int(input())
    data = []
    for i in range(100):
        d = input()
        data.append(list(d))

    data2 = []
    for i in range(100):
        dd = []
        for j in range(100):
            dd.append(data[j][i])
        data2.append(dd)

    i = 100 # 길이
    length = 0
    while i > 0:
        j = 0 # j번째 줄
        while j < 100:
            for k in range(i-1, 100): # 길이에 따른 반복 횟수
                start = k-(i-1)
                a = data[j][start:start+i]
                b = data2[j][start:start+i]
                if a == a[::-1]:
                    length = len(a)
                    break
                if b == b[::-1]:
                    length = len(b)
                    break
            j += 1
            if length != 0:
                break
        i -= 1
        if length != 0:
            break

    print('#{} {}'.format(tc+1, length))
