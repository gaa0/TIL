import sys
sys.stdin = open("글자수_input.txt")

T = int(input())
for tc in range(T):
    str1 = list(input())
    str2 = list(input())
    d = {}
    for i in str1:
        d[i] = 0
    for key in str2:
        if key in d.keys():
            d[key] += 1
    ans = 0
    for key, value in d.items():
        if value > ans:
            ans = value

    print('#{} {}'.format(tc+1, ans))
