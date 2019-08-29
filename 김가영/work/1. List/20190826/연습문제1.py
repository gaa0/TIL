su = input()
sul = list(su)
st = []

i = 0
while i < len(su):
    if '0' <= sul[i] <= '9':
        print(sul[i], end='')
    else:
        st.append(sul[i])

    i += 1

for i in range(len(st)):
    print(st.pop(), end='')