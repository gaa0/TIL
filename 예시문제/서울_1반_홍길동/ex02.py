# 파일명 및 함수명을 변경하지 마시오.
def calc(equation):
    """
    아래에 코드를 작성하시오.
    equation은 덧셈 뺄셈으로 이루어진 수식 문자열입니다.
    계산된 결과를 정수로 반환합니다.
    """
    c = equation.split('+')
    a = []
    d = []
    for i in range(len(c)):
        if '-' in c[i]:
            a.append(c[i].split('-'))
        else:
            if c[i] == '':
                c[i] = 0
            d.append(int(c[i]))
    b = []
    for j in range(len(a)):
        if a[j][0] == '':
            a[j][0] = 0
        d.append(int(a[j][0])-int(a[j][1]))
    return sum(d)




# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(calc('123+2-124'))
    print(calc('-12+12-7979+9191'))
    print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))