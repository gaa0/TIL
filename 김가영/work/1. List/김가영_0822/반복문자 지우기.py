import sys
sys.stdin = open('반복문자 지우기_input.txt')

T = int(input())
for tc in range(T):
    data = input()

    i = 0
    while i < len(data)-1:
        if len(data) <= 1:
            break
        if data[i] == data[i+1]:
            if i + 1 == len(data):
                data = data.replace(data[i]*2, '')
                break
            else:
                data = data.replace(data[i]*2, '')
                i = 0
                continue
        else:
            i += 1

    print('#{} {}'.format(tc+1, len(data)))
