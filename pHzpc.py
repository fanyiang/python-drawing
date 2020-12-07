# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:18:33 2020

@author: fanyiang
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from pylab import *


x=np.array([3.7,5.3,6.54,7.13,8.99])
x2=np.array([5.79,6.32,6.98,7.23,7.68])
y=x2-x
print(y)

fig, ax = plt.subplots()
ax.plot(x, y,'o-', color='r',linewidth=1,markersize=8)
ax.spines['bottom'].set_position(('data',0))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.xlabel('pH', fontdict={'family' : 'Arial', 'size'   : 16}) #X label 字体设置
plt.ylabel('$\mathregular{pH_{final-initial}}$', fontdict={'family' : 'Arial', 'size'   : 16})  #Y label 字体设置
plt.xticks(fontproperties = 'Arial', size = 12) #X轴 字体设置
plt.yticks(fontproperties = 'Arial', size = 12) #Y轴 字体设置

plt.show()
fig.savefig('pHzpc.png',dpi=600,format='png')

im = array(Image.open('pHzpc.png'))
imshow(im)
print('Please click screen')
x3=ginput(1)
print('The point you clicked:',x3)

y1=7.23-7.13
y2=7.69-8.99
k=(y2-y1)/(8.99-7.13)
b=y1-k*7.13
print('y=k*x+b',k,b)
x_cross=-1*b/k
print('与横坐标交点为：',x_cross)
