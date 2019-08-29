import sys
sys.stdin = open('계산기3_input.txt')

for tc in range(10):
    N = int(input())
    data = input()
    st = []
    hu = ''

    for i in data:
        if '0' <= i <= '9':
            # print(i, end='')
            hu += i
        else:
            if not st:
                st.append(i)
            else:
                if i == '(':
                    st.append(i)
                elif i == '*':
                    st.append(i)
                elif i == '+':
                    while 1:
                        if st:
                            if st[-1] == '*':
                                p = st.pop()
                                # print(p, end='')
                                hu += p
                            elif st[-1] == '+':
                                p = st.pop()
                                # print(p, end='')
                                hu += p
                            else:
                                st.append(i)
                                break
                        else:
                            st.append(i)
                            break
                elif i == ')':
                    while 1:
                        if st[-1] != '(':
                            p = st.pop()
                            # print(p, end='')
                            hu += p
                        if st[-1] == '(':
                            st.pop()
                            break

    while st:
        p = st.pop()
        # print(p, end='')
        hu += p

    st = []
    for i in hu:
        if '0' <= i <= '9':
            st.append(i)
        else:
            if i == '+':
                a = st.pop()
                b = st.pop()
                sik = int(a) + int(b)
                st.append(str(sik))
            elif i == '*':
                a = st.pop()
                b = st.pop()
                sik = int(a)*int(b)
                st.append(str(sik))

    ans = st.pop()
    print('#{} {}'.format(tc+1, ans))
