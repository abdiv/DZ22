a = 'dkfjjhkjbggkljhlkjhddddlhjlkjgvvkjbljbeeekjhss'
e = len(a)
b = list(a)
d = []
k = 1
for x in range(e-1):
    if b[x] == b[x+1]:
        k = k+1
        d.append(k)
    else:
        k = 1
        d.append(k)
ddd = max(d)
print(ddd)

