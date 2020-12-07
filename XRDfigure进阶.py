# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:33:39 2020

@author: fanyiang
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



x0value=locals()
xvalue=locals()
y0value=locals()
yvalue=locals()
for i in range(1,4):
        
    x0value['x'+str(i)]=pd.read_csv('F:/学习/CoP@C/paper/XRD总.csv',header=None,usecols=[2*i-2]) #x1-x3是三组横坐标
    xvalue['x'+str(i)]=np.array(x0value['x'+str(i)])
    
    y0value['y'+str(i)]=pd.read_csv('F:/学习/CoP@C/paper/XRD总.csv',header=None,usecols=[2*i-1])  #y1-y3是三组纵坐标
    yvalue['y'+str(i)]=np.array(y0value['y'+str(i)])
   
    
   
    
fig=plt.figure(figsize=(5.36,4.1025),dpi=600)  #画一个图层

#XRD画在最大的图层中，卡片从最下面依次堆叠
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8],facecolor='none')  # left, bottom, width, height (range 0 to 1)
axes1 = fig.add_axes([0.1, 0.3, 0.8, 0.2],facecolor='none')  #卡片1,上
axes2 = fig.add_axes([0.1, 0.1, 0.8, 0.2],facecolor='none')  #卡片2，下,facecolor设为none，图层透明，防止上面的图层覆盖下面的


markerline, stemlines, baseline=axes2.stem(x3,y3, markerfmt=' ', basefmt = '-', use_line_collection=True)
plt.setp(stemlines, linewidth=2, color='dimgray') #最下面，用stem函数画茎图，y坐标向x垂线

markerline, stemlines, baseline=axes1.stem(x2,y2, markerfmt=' ', basefmt = '-', use_line_collection=True)
plt.setp(stemlines, linewidth=2, color='#ff9b93')

plot=axes.plot(x1, y1,'-', color='#2d6187',linewidth=1.5) #XRD谱图


#各subplot分别设置

plt.sca(axes2)  
plt.xlim(10,90) #最下图坐标范围
plt.ylim(0,100)
plt.yticks([])
plt.xticks([])
#plt.hlines(0, 10, 90,colors = "dimgrey")
frame = plt.gca() #读取当前图层
frame.spines['top'].set_visible(False)  #上框线不显示
frame.spines['bottom'].set_visible(False)
plt.text(63,35,'JCPDS  No. 46-0943 \nCarbon',fontdict={'family' : 'Arial', 'size'   : 10}) #pdf卡片号，添加文本即可


plt.sca(axes) #大图
plt.xlim(10,90)
plt.ylim(-400,1500)
plt.ylabel('Intensity  (a.u.)',fontdict={'family' : 'Arial', 'size'   : 20})
plt.xticks(fontproperties = 'Arial', size = 16) #X轴 字体设置
plt.xlabel('2 Theta (degree)', fontdict={'family' : 'Arial', 'size'   : 20}) #X label 字体设置
plt.yticks([])
frame = plt.gca()
frame.spines['bottom'].set_visible(True)


plt.sca(axes1) #中间图设置 
plt.xlim(10,90) #中间坐标范围
plt.xticks([])
plt.yticks([]) 
plt.hlines(0, 10, 90,colors = "#ff9b93") #y=0的水平横线，括号第一个数字为y，第二和第三个数字为x的起始点
frame = plt.gca()
frame.spines['bottom'].set_visible(False)
frame.spines['top'].set_visible(False)
plt.text(63,25,'JCPDS  No. 77-0263 \n$\mathregular{CoP_{2}}$',fontdict={'family' : 'Arial', 'size'   : 10}) #pdf卡片号，添加文本即可

plt.show()
fig.savefig('XRDpython.tif',dpi=600,format='tif',bbox_inches = 'tight') #bbox_inches 为tight时，可以确保输出图片完整

print('Done!')




