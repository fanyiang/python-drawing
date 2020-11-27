# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:53:15 2020

@author: fanyiang
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df0 = pd.read_csv('F:/学习/CoAl2O4 ceramic membrane/figure/xpstest.csv',header=None)

print(df0.head())

df_name = locals()
for i in range(1,11):
    df_name['df'+str(i)] = pd.read_csv('F:/学习/CoAl2O4 ceramic membrane/figure/xpstest.csv',header=None,usecols=[i-1])

    print (df_name['df'+str(i)].head())

#df1 = pd.read_csv('F:/学习/CoAl2O4 ceramic membrane/figure/xpstest.csv',header=None,usecols=[0])
#df2 = pd.read_csv('F:/学习/CoAl2O4 ceramic membrane/figure/xpstest.csv',header=None,usecols=[1])
#df3 = pd.read_csv('F:/学习/CoAl2O4 ceramic membrane/figure/xpstest.csv',header=None,usecols=[2])
#df4 = pd.read_csv('F:/学习/CoAl2O4 ceramic membrane/figure/xpstest.csv',header=None,usecols=[3])
#df5 = pd.read_csv('F:/学习/CoAl2O4 ceramic membrane/figure/xpstest.csv',header=None,usecols=[4])
#df6 = pd.read_csv('F:/学习/CoAl2O4 ceramic membrane/figure/xpstest.csv',header=None,usecols=[5])
#df7 = pd.read_csv('F:/学习/CoAl2O4 ceramic membrane/figure/xpstest.csv',header=None,usecols=[6])
#df8 = pd.read_csv('F:/学习/CoAl2O4 ceramic membrane/figure/xpstest.csv',header=None,usecols=[7])
#df9 = pd.read_csv('F:/学习/CoAl2O4 ceramic membrane/figure/xpstest.csv',header=None,usecols=[8])
#df10 = pd.read_csv('F:/学习/CoAl2O4 ceramic membrane/figure/xpstest.csv',header=None,usecols=[9])

#print(df1.head())
#print(df2.head())


X0=np.array(df_name['df1'])
Y01=np.array(df_name['df2'])
Y02=np.array(df_name['df3'])
Y03=np.array(df_name['df4'])
Y04=np.array(df_name['df5'])
Y05=np.array(df_name['df6'])
Y06=np.array(df_name['df7'])
Y07=np.array(df_name['df8'])
Y08=np.array(df_name['df9'])
Y09=np.array(df_name['df10'])


X = X0[:,0]  #转置
Y1 = Y01[:,0]
Y2 = Y02[:,0]
Y3 = Y03[:,0]
Y4 = Y04[:,0]
Y5 = Y05[:,0]
Y6 = Y06[:,0]
Y7 = Y07[:,0]
Y8 = Y08[:,0]
Y9 = Y09[:,0]

fig, ax = plt.subplots()
ax.invert_xaxis()
plt.xlim(808, 775) #set X range
ax.plot(X, Y1, X, Y8, X, Y9, color='dimgray',linewidth=0.5)
ax.plot(X, Y2, X, Y3, X, Y4, X, Y5, X, Y6, X, Y7, color='none',linewidth=0.5)

ax.fill_between(X, Y2, Y8, facecolor='#9ad3bc',alpha=0.6)
ax.fill_between(X, Y3, Y8, facecolor='red')
ax.fill_between(X, Y4, Y8, facecolor='lightcoral',alpha=0.6)
ax.fill_between(X, Y5, Y8, facecolor='cornflowerblue',alpha=0.6)
ax.fill_between(X, Y6, Y8, facecolor='#ffdd93',alpha=0.8)
ax.fill_between(X, Y7, Y8, facecolor='#ffa36c',alpha=0.6)
plt.xlabel('Binding energy (eV)', fontdict={'family' : 'Arial', 'size'   : 16}) #X label 字体设置
plt.ylabel('Counts (s)', fontdict={'family' : 'Arial', 'size'   : 16})  #Y label 字体设置
plt.xticks(fontproperties = 'Arial', size = 12) #X轴 字体设置
plt.yticks(fontproperties = 'Arial', size = 12) #Y轴 字体设置

plt.show()
fig.savefig('XPS-Co1.tif',dpi=600,format='tif')
fig.savefig('XPS-Co1.png',dpi=600,format='png')
print('done!')