# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 16:48:58 2023

@author: YG168VL
"""

import pandas as pd
import numpy as np
import random
random.seed(12)
np.random.seed(12)
def generate_random_timeseries_data(proportion_to_delete=0.2):
    date_range=pd.date_range(start='2020-01-01',end='2021-01-20',freq='B')
    random_data=np.random.rand(len(date_range))
    timeseries_data=pd.DataFrame({'Date':date_range,'Value':random_data})
    num_obs_to_delete=int(proportion_to_delete*len(timeseries_data))
    #print("num=",num_obs_to_delete)
    indices_to_delete=np.random.choice(timeseries_data.index,num_obs_to_delete,replace=False)
    #print(indices_to_delete)
    timeseries_data.drop(indices_to_delete,inplace=True)
    return timeseries_data

 

def nrst_tenth_business_days(data):
    #print(len(data))
    tens={}
    #print(Dt_1,"---",Dt_2)
    for x in range(len(data)-20):
        diff=[]
        Dt=data.Date.iloc[x]
        for j in range(x+1,len(data)):#Dt_Dash
            Dt_dash=data.Date.iloc[j]
            diff.append((Dt_dash-Dt).days) 
        #print(diff)
        minimise=abs((10/np.array(diff))-1)
        #print(minimise)
        tens[x]=x+np.argmin(minimise)
        print(tens)
        return tens
    return(tens)

if __name__=="__main__":
    data=generate_random_timeseries_data()
    dates=nrst_tenth_business_days(data)
    ret=[]
    for dt,dtdash in dates.items():
        ret.append(np.log(data.Value.iloc[dtdash]/data.Value.iloc[dt])*((10/(dtdash-dt))**0.5))
    print(ret)