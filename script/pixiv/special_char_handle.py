# -*- coding: utf-8 -*-
import time

a = "a?b"
b = "b*c"
c = "c:d"
d = "d\"e"
e = "e<f"
f = "f>g"
g = "g\\h"
h = "h/i"
i = "i|j"

print(a.replace('?', 'AX'))
print(b.replace('*', 'BX'))
print(c.replace(':', 'CX'))
print(d.replace('\"', 'DX'))
print(e.replace('<', 'EX'))
print(f.replace('>', 'FX'))
print(g.replace('\\', 'GX'))
print(h.replace('/', 'HX'))
print(i.replace('|', 'IX'))

# with open('/Volumes/Common/test/aaa:xx', "w"):
#     pass

print(time.strftime('%Y%m%d%H', time.localtime()))
