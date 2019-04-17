a = 'Вскоре после восхода солнца выдалось чистое ясное утро'
b = a.split(' ')
d = []
g = []
for x in b:
    #c = len(x)
    d.append(len(x))
с = min(d)
for k in b:
    #f = len(k)
    if len(k) > с:
        f = k.replace(k[с::], '*')
        e = f.ljust(len(k), '*')
        g.append(e)
    else:
        f = k.replace(k[с::], '')
        e = f
        g.append(e)
    gg = ' '.join(g)
print(gg)
