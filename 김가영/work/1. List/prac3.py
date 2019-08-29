def bruteForce(pattern, text):
    M = len(pattern)
    N = len(text)
    i = 0
    j = 0
    while j < M and i < N:
        if text[i] != pattern[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if i == M:
        return i - M
    else:
        return -1

def bruteForce2(text, pattern):
    for i in range(len(text)-len(pattern)+1):
        cnt = 0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            else: cnt += 1
        if cnt >= len(pattern):
            return i
    return -1


text = "TTTTAACCA"
pattern = "TTA"
print("{}".format(bruteForce(text, pattern)))
print("{}".format(bruteForce2(text, pattern)))
print(text.find(pattern))