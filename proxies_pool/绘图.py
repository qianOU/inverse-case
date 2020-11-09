# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:34:30 2019

@author: Administrator
"""
import numpy as np
import  copy
import pandas as  pd
import math
from matplotlib import pyplot as plt
w=pd.read_excel('Heroin.xlsx')
lon=len(w.index)   
#s={'pai_min':j,'text':[]}
t={1:'1st',2:'2nd',3:'3rd',4:'4th'}
for j in range(5):  
    s={'pai_min':j,'text':[],'score':[]}
    for i in range(j,lon,5):
        s['text'].append(w.ix[i,'county']+','+w.ix[i,'state'])
        s['score'].append(w.ix[i,'score'])
    plt.plot(s['score'],lebel='ranked %s'%t[j])
    for q in range(8):
        plt.text(q,s['score'][q],text=s['text'][q],fontsize=8,ha='center')
        
            
    