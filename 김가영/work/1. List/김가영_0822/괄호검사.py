import sys
sys.stdin = open('괄호검사_input.txt')

T = int(input())
for tc in range(T):
    data = input()

    s = []


    def isEmpty():
        if len(s) == 0:
            return 1
        else:
            return 0


    def check_matching_data(data):
        for i in data:
            if i == '(' or i == ')' or i == '{' or i == '}':
                if i == '(':
                    s.append(i)
                elif i == '{':
                    s.append(i)
                elif i == '}':
                    if s and s[-1] == '{':
                        s.pop()
                    else:
                        return 0
                elif i == ')':
                    if s and s[-1] == '(':
                        s.pop()
                    else:
                        return 0
        return isEmpty()


    print('#{} {}'.format(tc+1, check_matching_data(data)))
