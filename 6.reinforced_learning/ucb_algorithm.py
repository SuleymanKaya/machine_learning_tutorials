# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:58:44 2019

@author: suleyman.kaya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler=pd.read_csv('reklamverisi.csv')

#Upper Confidence Bound (UCB) Algoritması

import math

N = 10000 # 10.000 tıklama
d = 10  # toplam 10 ilan var
oduller = [0] * d #ilk basta butun ilanların odulu 0
tiklamalar = [0] * d #o ana kadarki tıklamalar
toplam = 0 # toplam odul
secilenler = []
for n in range(0,N):
    ad = 0 #seçilen ilan
    max_ucb = 0
    for i in range(0,d):
        if(tiklamalar[i] > 0):
            ortalama = oduller[i] / tiklamalar[i]
            delta = math.sqrt(3/2* math.log(n)/tiklamalar[i])
            ucb = ortalama + delta
        else:
            ucb = N*10
        if max_ucb < ucb: #max'tan büyük bir ucb çıktı
            max_ucb = ucb
            ad = i 
            
    secilenler.append(ad)
    tiklamalar[ad] = tiklamalar[ad]+ 1
    odul = veriler.values[n,ad] # verilerdeki n. satır = 1 ise odul 1
    oduller[ad] = oduller[ad]+ odul
    toplam = toplam + odul
    
print('Toplam Odul:')   
print(toplam)

plt.hist(secilenler)
plt.show()


