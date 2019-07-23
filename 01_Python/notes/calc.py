def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiplication(a, b):
    return a*b

def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "문자열 '0'으로는 나눌 수 없습니다."