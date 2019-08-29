a = '()()((()))'
b = '((()((((()()((()())((())))))'


s = []


def isEmpty():
    if len(s) == 0:
        return True
    else:
        return False


def check_matching(data):
    for i in data:
        if i == '(':
            s.append('(')
        elif i == ')':
            s.pop()
    return isEmpty()


data = b
print(check_matching(data))