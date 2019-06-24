# -*- coding: utf-8 -*-

style = 'background-color:#f9f4dc;box-shadow:0 15px 30px 0 rgba(249,244,220,.8)'

color = style[17:24]
print(color)

print(color[1:3])
print(color[3:5])
print(color[5:7])

print(int(color[1:3], 16))
print(int(color[3:5], 16))
print(int(color[5:7], 16))

c = '#f90'
x = c[1:2]
y = c[2:3]
z = c[3:4]

x = x + x
y = y + y
z = z + z

print(x + y + z)
