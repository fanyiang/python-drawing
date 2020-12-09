# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:36:54 2020

@author: fanyiang
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap,LinearSegmentedColormap
import matplotlib as mpl
import pandas as pd

fig, ax = plt.subplots(dpi=96)
ax.set(xlim=(1,10), ylim=(-0.1,101), autoscale_on=False)

#a = np.array([[1, 1],
              #[2, 2],
              #[3, 3],
              #[4, 4],
              #[5, 5]])  #每种渐变色分成五段（array五行），数字表示在colormap对应的深浅
avalue=locals() 
dfvalue=locals()            
for i in range(1,101):
    avalue['a'+str(i)]=np.array([[i,i]]) #渐变色分为100段，分的更细
    dfvalue['df'+str(i)]=pd.DataFrame(avalue['a'+str(i)]) #转dataframe
    df=dfvalue['df'+str(i)]
    df.to_csv("temp.csv", mode='a',header=None) #暂存csv文件，第一列会把每一次循环的index放进去
df3=pd.read_csv('temp.csv',header=None)#读取csv
df3.columns=['序号','x','y']#column命名，第一列废弃
df3=df3.drop('序号',axis=1)#删除第一列
a=np.array(df3) #转array
print(df3.head())

                                                                                                                                           
                                                                                                                                   
#a=np.vstack((a1,a2,a3,a4,a5,a6,a7,a8,a9,a10))

print(a)

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
