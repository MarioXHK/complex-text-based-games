import matplotlib.pyplot as p1t
import numpy as np

x = []
y = []
x0 = []
y0 = []
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
xb = []
yb = []

for i in np.arange(-10, 11, .01):
    x.append(np.sin(3*i))
    
for i in np.arange(-10, 11, .01):
    y.append(np.sin(4*i))

for i in np.arange(-10, 11, .01):
    x0.append((i**3)-(2*i))
    
for i in np.arange(-10, 11, .01):
    y0.append((i**2)-i)

for i in np.arange(-10, 11, .01):
    x1.append((i**4)-(i**2))
    
for i in np.arange(-10, 11, .01):
    y1.append(i+np.log(i))

for i in np.arange(-10, 11, .01):
    x2.append(i+np.sin(2*i))
    
for i in np.arange(-10, 11, .01):
    y2.append(i+np.sin(3*i))
for i in np.arange(-10, 11, .01):
    x3.append(np.sin(i + np.sin(i)))
    
for i in np.arange(-10, 11, .01):
    y3.append(np.cos(i + np.cos(i)))

for i in np.arange(-10, 11, .01):
    x4.append(np.cos(i))
    
for i in np.arange(-10, 11, .01):
    y4.append(np.sin(i + np.sin(5*i)))

for i in np.arange(-10, 11, .01):
    xb.append(np.cos(i))
    
for i in np.arange(-10, 11, .01):
    yb.append(np.cos(i + np.cos(5*i)))

p1t.plot(x,y)#V is for c
p1t.plot(x0,y0)#a is vor IV
p1t.plot(x1,y1)#b is for VI
p1t.plot(x2,y2)#d is for III
p1t.plot(x3,y3)#e is for I
#so f should be for II
p1t.plot(x4,y4)
#BONUS because it looked cool when I messed up the 6th
p1t.plot(xb,yb)

p1t.show()