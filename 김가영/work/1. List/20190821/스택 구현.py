s = []


def push(item):
    s.append(item)


def pop():
    if len(s) == 0:
        return
    else:
        return s.pop(-1)


push(1)
print(s)
push(2)
print(s)
push(3)
print(s)
pop()
print(s)
pop()
print(s)
pop()
print(s)
