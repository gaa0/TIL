import sys

sys.stdin = open('Forth_input.txt')

T = int(input())
for tc in range(T):
    data = list(map(str, input().split()))
    st = []

    for i in data:
        try:
            try:
                if int(i):
                    st.append(int(i))
            except ValueError:
                if i == '+':
                    st.append(st.pop() + st.pop())
                elif i == '-':
                    a = st.pop()
                    b = st.pop()
                    st.append(b - a)
                elif i == '*':
                    st.append(st.pop()*st.pop())
                elif i == '/':
                    a = st.pop()
                    b = st.pop()
                    st.append(b//a)
                elif i == '.':
                    if len(st) >= 2:
                        ans = 'error'
                    else:
                        ans = st.pop()
        except:
            ans = 'error'

    print('#{} {}'.format(tc + 1, ans))
