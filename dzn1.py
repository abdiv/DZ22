for x1 in range(1, 1000000):
    a = str(x1)
    b = a.rjust(6, '0')
    if (int(b[0])+int(b[1])+int(b[2])) == (int(b[3])+int(b[4])+int(b[5])):
       print(b)
