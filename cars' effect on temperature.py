
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt

#Input_Temperature
Temp_Moscow       = pd.read_csv('TempMoscow.csv', index_col='DATE', parse_dates=True)
Temp_Mozhaisk     = pd.read_csv('TempMozhaisk.csv', index_col='DATE', parse_dates=True)
Temp_Berlin       = pd.read_csv('TempBerlin.csv', index_col='DATE', parse_dates=True)
Temp_Altentreptow = pd.read_csv('TempAltentreptow.csv', index_col='DATE', parse_dates=True)
Temp_LosAngeles   = pd.read_csv('TempLosAngeles.csv', index_col='DATE', parse_dates=True)
Temp_SantaBarbara = pd.read_csv('TempSantaBarbara.csv', index_col='DATE', parse_dates=True)

#Input_Car
Car_Moscow       = pd.read_excel('moscow.xls',index_col='year',parse_dates=True,encoding='cp1251')
Car_Mozhaisk     = pd.read_excel('autoMozhaisk.xls',index_col='year',parse_dates=True)
Car_Berlin       = pd.read_excel('berlin.xls',index_col='year',parse_dates=True)
Car_Altentreptow = pd.read_excel('town_berlin.xls',index_col='year',parse_dates=True)
Car_LosAngeles   = pd.read_excel('los angeles11.xls',index_col='year',parse_dates=True,encoding='cp1251')
Car_SantaBarbara = pd.read_excel('santa barbara.xls',index_col='year',parse_dates=True)


#Temp_Moscow_changed
Temp_Moscow_Changed = Temp_Moscow.drop(['STATION', 'NAME'],axis='columns')
Temp_Moscow_Changed['AVG'] = (Temp_Moscow_Changed['TMAX'] + Temp_Moscow_Changed['TMIN']) // 2
Temp_Moscow_Changed['TMAX'].replace('', np.nan, inplace=True)
Temp_Moscow_Changed['TMIN'].replace('', np.nan, inplace=True)
Temp_Moscow_Changed.dropna(subset=['TMAX'], inplace=True)
Temp_Moscow_Changed.dropna(subset=['TMIN'], inplace=True)

#Temp_Mozhaisk_changed
Temp_Mozhaisk_Changed = Temp_Mozhaisk.drop(['STATION', 'NAME'],axis='columns')
Temp_Mozhaisk_Changed['AVG'] = (Temp_Mozhaisk_Changed['TMAX'] + Temp_Mozhaisk_Changed['TMIN']) // 2
Temp_Mozhaisk_Changed['TMAX'].replace('', np.nan, inplace=True)
Temp_Mozhaisk_Changed['TMIN'].replace('', np.nan, inplace=True)
Temp_Mozhaisk_Changed.dropna(subset=['TMAX'], inplace=True)
Temp_Mozhaisk_Changed.dropna(subset=['TMIN'], inplace=True)

#Temp_Berlin_changed
Temp_Berlin_Changed = Temp_Berlin.drop(['STATION', 'NAME'],axis='columns')
Temp_Berlin_Changed['AVG'] = (Temp_Berlin_Changed['TMAX'] + Temp_Berlin_Changed['TMIN']) // 2
Temp_Berlin_Changed['TMAX'].replace('', np.nan, inplace=True)
Temp_Berlin_Changed['TMIN'].replace('', np.nan, inplace=True)
Temp_Berlin_Changed.dropna(subset=['TMAX'], inplace=True)
Temp_Berlin_Changed.dropna(subset=['TMIN'], inplace=True)

#Temp_Altentreptow_changed
Temp_Altentreptow_Changed = Temp_Altentreptow.drop(['STATION', 'NAME'],axis='columns')
Temp_Altentreptow_Changed['AVG'] = (Temp_Altentreptow_Changed['TMAX'] + Temp_Altentreptow_Changed['TMIN']) // 2
Temp_Altentreptow_Changed['TMAX'].replace('', np.nan, inplace=True)
Temp_Altentreptow_Changed['TMIN'].replace('', np.nan, inplace=True)
Temp_Altentreptow_Changed.dropna(subset=['TMAX'], inplace=True)
Temp_Altentreptow_Changed.dropna(subset=['TMIN'], inplace=True)

#Temp_LosAngeles_changed
Temp_LosAngeles_Changed = Temp_LosAngeles.drop(['STATION', 'NAME'],axis='columns')
Temp_LosAngeles_Changed['AVG'] = (Temp_LosAngeles_Changed['TMAX'] + Temp_LosAngeles_Changed['TMIN']) // 2
Temp_LosAngeles_Changed['TMAX'].replace('', np.nan, inplace=True)
Temp_LosAngeles_Changed['TMIN'].replace('', np.nan, inplace=True)
Temp_LosAngeles_Changed.dropna(subset=['TMAX'], inplace=True)
Temp_LosAngeles_Changed.dropna(subset=['TMIN'], inplace=True)

#Temp_SantsBarbara_changed
Temp_SantaBarbara_Changed = Temp_SantaBarbara.drop(['STATION', 'NAME'],axis='columns')
Temp_SantaBarbara_Changed['AVG'] = (Temp_SantaBarbara_Changed['TMAX'] + Temp_SantaBarbara_Changed['TMIN']) // 2
Temp_SantaBarbara_Changed['TMAX'].replace('', np.nan, inplace=True)
Temp_SantaBarbara_Changed['TMIN'].replace('', np.nan, inplace=True)
Temp_SantaBarbara_Changed.dropna(subset=['TMAX'], inplace=True)
Temp_SantaBarbara_Changed.dropna(subset=['TMIN'], inplace=True)


#Temp_Moscow_ChangedYear and Temp_Moscow_ChangedMonth
Temp_Moscow_ChangedYear  = Temp_Moscow_Changed.resample('Y')['AVG'].mean()
Temp_Moscow_ChangedMonth = Temp_Moscow_Changed.resample('M')['AVG'].mean()

#Temp_Mozhaisk_ChangedYear and Temp_Mozhaisk_ChangedMonth
Temp_Mozhaisk_ChangedYear  = Temp_Mozhaisk_Changed.resample('Y')['AVG'].mean()
Temp_Mozhaisk_ChangedMonth = Temp_Mozhaisk_Changed.resample('M')['AVG'].mean()

#Temp_Berlin_ChangedYear and Temp_Berlin_ChangedMonth
Temp_Berlin_ChangedYear  = Temp_Berlin_Changed.resample('Y')['AVG'].mean()
Temp_Berlin_ChangedMonth = Temp_Berlin_Changed.resample('M')['AVG'].mean()


#Temp_Altentreptow_ChangedYear and Temp_Altentreptow_ChangedMonth
Temp_Altentreptow_ChangedYear  = Temp_Altentreptow_Changed.resample('Y')['AVG'].mean()
Temp_Altentreptow_ChangedMonth = Temp_Altentreptow_Changed.resample('M')['AVG'].mean()

#Temp_LosAngeles_ChangedYear and Temp_LosAngeles_ChangedMonth
Temp_LosAngeles_ChangedYear  = Temp_LosAngeles_Changed.resample('Y')['AVG'].mean()
Temp_LosAngeles_ChangedMonth = Temp_LosAngeles_Changed.resample('M')['AVG'].mean()

#Temp_SantaBarbara_ChangedYear and Temp_SantaBarbara_ChangedMonth
Temp_SantaBarbara_ChangedYear  = Temp_SantaBarbara_Changed.resample('Y')['AVG'].mean()
Temp_SantaBarbara_ChangedMonth = Temp_SantaBarbara_Changed.resample('M')['AVG'].mean()


#Car_Moscow_Sort   = Car_Moscow.sort_index()
#Car_Mozhaisk_Sort = Car_Mozhaisk.sort_index()

Square_Moscow       = 2561
Square_Mozhaisk     = 18
Square_Berlin       = 891
Square_Altentreptow = 53
Square_LosAngeles   = 1301
Square_SantaBarbara = 111

Car_Moscow['cars/sqr km']       = Car_Moscow['total cars'] // Square_Moscow
Car_Mozhaisk['cars/sqr km']     = Car_Mozhaisk['total cars'] // Square_Mozhaisk
Car_Berlin['cars/sqr km']       = Car_Berlin['total number'] // Square_Berlin
Car_Altentreptow['cars/sqr km'] = Car_Altentreptow['total number'] // Square_Altentreptow
Car_LosAngeles['cars/sqr km']   = Car_LosAngeles['total number'] // Square_LosAngeles
Car_SantaBarbara['cars/sqr km'] = Car_SantaBarbara['total number'] // Square_SantaBarbara

Car_Moscow_Changed       = Car_Moscow['cars/sqr km']
Car_Mozhaisk_Changed     = Car_Mozhaisk['cars/sqr km']
Car_Berlin_Changed       = Car_Berlin['cars/sqr km']
Car_Altentreptow_Changed = Car_Altentreptow['cars/sqr km']
Car_LosAngeles_Changed   = Car_LosAngeles['cars/sqr km']
Car_SantaBarbara_Changed = Car_SantaBarbara['cars/sqr km']


# In[8]:


#trace_Temp_Moscow_Mozhaisk
trace_Temp_Moscow = go.Scatter(
    x = Temp_Moscow_ChangedYear.index,
    y = Temp_Moscow_ChangedYear.values,
    name = 'Среднее по годам'
)
trace_Temp_Mozhaisk = go.Scatter(
    x = Temp_Mozhaisk_ChangedYear.index,
    y = Temp_Mozhaisk_ChangedYear.values,
    name = 'Среднее по годам'
)

#trace_Temp_Berlin_Altentreptow
trace_Temp_Berlin = go.Scatter(
    x = Temp_Berlin_ChangedYear.index,
    y = Temp_Berlin_ChangedYear.values,
    name = 'Среднее по годам'
)
trace_Temp_Altentreptow = go.Scatter(
    x = Temp_Altentreptow_ChangedYear.index,
    y = Temp_Altentreptow_ChangedYear.values,
    name = 'Среднее по годам'
)

#trace_Temp_LosAngeles_SantaBarbara
trace_Temp_LosAngeles = go.Scatter(
    x = Temp_LosAngeles_ChangedYear.index,
    y = Temp_LosAngeles_ChangedYear.values,
    name = 'Среднее по годам'
)
trace_Temp_SantaBarbara = go.Scatter(
    x = Temp_SantaBarbara_ChangedYear.index,
    y = Temp_SantaBarbara_ChangedYear.values,
    name = 'Среднее по годам'
)

#trace_Car_Moscow_Mozhaisk
trace_Car_Moscow = go.Scatter(
    x = Car_Moscow_Changed.index,
    y = Car_Moscow_Changed.values,
    name = 'Среднее по годам'
)
trace_Car_Mozhaisk = go.Scatter(
    x = Car_Mozhaisk_Changed.index,
    y = Car_Mozhaisk_Changed.values,
    name = 'Среднее по годам'
)

#trace_Car_Berlin_Altentreptow
trace_Car_Berlin = go.Scatter(
    x = Car_Berlin_Changed.index,
    y = Car_Berlin_Changed.values,
    name = 'Среднее по годам'
)
trace_Car_Altentreptow = go.Scatter(
    x = Car_Altentreptow_Changed.index,
    y = Car_Altentreptow_Changed.values,
    name = 'Среднее по годам'
)

#trace_Car_LosAngeles_SantaBarbara
trace_Car_LosAngeles = go.Scatter(
    x = Car_LosAngeles_Changed.index,
    y = Car_LosAngeles_Changed.values,
    name = 'Среднее по годам'
)
trace_Car_SantaBarbara = go.Scatter(
    x = Car_SantaBarbara_Changed.index,
    y = Car_SantaBarbara_Changed.values,
    name = 'Среднее по годам'
)

fig = py.tools.make_subplots(rows=2, cols=3, subplot_titles=('Москва и Можайск', 'Берлин и Альтентрептов', 'Лос-Анджелес и Санта-Барбара'))
#Temperature
fig.append_trace(trace_Temp_Moscow, 1, 1)
fig.append_trace(trace_Temp_Mozhaisk, 1, 1)
fig.append_trace(trace_Temp_Berlin, 1, 2)
fig.append_trace(trace_Temp_Altentreptow, 1, 2)
fig.append_trace(trace_Temp_LosAngeles, 1, 3)
fig.append_trace(trace_Temp_SantaBarbara, 1, 3)
#Car
fig.append_trace(trace_Car_Moscow, 2, 1)
fig.append_trace(trace_Car_Mozhaisk, 2, 1)
fig.append_trace(trace_Car_Berlin, 2, 2)
fig.append_trace(trace_Car_Altentreptow, 2, 2)
fig.append_trace(trace_Car_LosAngeles, 2, 3)
fig.append_trace(trace_Car_SantaBarbara, 2, 3)

fig['layout'].update(height = 720, width = 1366, title = 'Результаты')
py.offline.plot(fig, filename = 'test.html', auto_open = True)

