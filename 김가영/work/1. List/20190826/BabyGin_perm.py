# arr = [6, 6, 7, 7, 6, 7]
arr = [1, 2, 4, 7, 8, 3]
# arr = [6, 5, 4, 0, 6, 0]
# arr = [1, 0, 1, 1, 2, 3]
def babyGin():
    global flag
    check = 0

    if arr[0] == arr[1] and arr[1] == arr[2]:
        check += 1
    if arr[3] == arr[4] and arr[4] == arr[5]:
        check += 1

    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
        check += 1
    if arr[3] + 1 == arr[4] and arr[4] + 1 == arr[5]:
        check += 1