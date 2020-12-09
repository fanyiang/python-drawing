# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:36:54 2020

@author: fanyiang
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap,LinearSegmentedColormap
import matplotlib as mpl

fig, ax = plt.subplots(dpi=96)
ax.set(xlim=(1,10), ylim=(-0.1,101), autoscale_on=False)

a = np.array([[1, 1],
              [2, 2],
              [3, 3],
              [4, 4],
              [5, 5]])  #每种渐变色分成五段（array五行），数字表示在colormap对应的深浅
print(a.shape)

clist=['white','blue'] #线性变化颜色由上面array值 小到大
clist2=['red','white']
newcmp = LinearSegmentedColormap.from_list('chaos',clist)
newcmp2 = LinearSegmentedColormap.from_list('chaos',clist2)


plt.imshow(a,cmap=newcmp,interpolation='bicubic',extent=(1,10,0,60))
plt.imshow(a,cmap=newcmp2,interpolation='bicubic',extent=(1,10,60,100)) #白色设置在60%处

frame = plt.gca() #读取当前图层
ax.yaxis.tick_right()  #纵坐标移到右边
ax.set_yticklabels(('-80','-60','-40','-20','0','20','40')) #自定义yticks显示的值，第一个label不显示
frame.spines['top'].set_visible(False)  #上框线不显示
frame.spines['bottom'].set_visible(False)
frame.spines['right'].set_visible(False)
frame.spines['left'].set_visible(False)
plt.xticks([]) #x坐标不要


plt.show()
fig.savefig('colorbar.tif',dpi=600,format='tif')
print('Done!')

#N = 10
#x = np.arange(N) + 0.15
#y = np.random.rand(N)

#width = 0.4
#for x, y in zip(x, y):
    #ax.imshow(a, interpolation='bicubic', extent=(x, x+width, 0, y), cmap=plt.cm.Blues_r)

#ax.set_aspect('auto')
#plt.show()
