import sys
sys.stdin = open("문자열비교_input.txt")


def bruteForce(text, pattern):
    i, j = 0, 0
    while i < len(text) and j < len(pattern):
        if text[i] != pattern[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == len(pattern):
        return 1
    else:
        return 0


T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()

    print('#{} {}'.format(tc+1, bruteForce(str2, str1)))
