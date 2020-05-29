

import pandas as pd
import numpy as
Temp_Moscow =       pd.read_csv('TempMoscow.csv')
Temp_Mozhaisk =     pd.read_csv('TempMozhaisk.csv')
Temp_Berlin =       pd.read_csv('TempBerlin.csv')
Temp_Altentreptow = pd.read_csv('TempAltentreptow.csv')
Temp_LosAngeles =   pd.read_csv('TempLosAngeles.csv')
Temp_SantaBarbara = pd.read_csv('TempSantaBarbara.csv')

#Temp_Moscow_changed
Temp_Moscow_Changed = Temp_Moscow.drop(['STATION', 'NAME'],axis='columns')
Temp_Moscow_Changed['AVG'] = (Temp_Moscow_Changed['TMAX']+Temp_Moscow_Changed['TMIN']) // 2
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
Temp_Altentreptow_changed = Temp_Altentreptow.drop(['STATION', 'NAME'],axis='columns')
Temp_Altentreptow_changed['AVG'] = (Temp_Altentreptow_changed['TMAX'] + Temp_Altentreptow_changed['TMIN']) // 2
Temp_Altentreptow_changed['TMAX'].replace('', np.nan, inplace=True)
Temp_Altentreptow_changed['TMIN'].replace('', np.nan, inplace=True)
Temp_Altentreptow_changed.dropna(subset=['TMAX'], inplace=True)
Temp_Altentreptow_changed.dropna(subset=['TMIN'], inplace=True)

#Temp_LosAngeles_changed
Temp_LosAngeles_changed = Temp_LosAngeles.drop(['STATION', 'NAME'],axis='columns')
Temp_LosAngeles_changed['AVG'] = (Temp_LosAngeles_changed['TMAX'] + Temp_LosAngeles_changed['TMIN']) // 2
Temp_LosAngeles_changed['TMAX'].replace('', np.nan, inplace=True)
Temp_LosAngeles_changed['TMIN'].replace('', np.nan, inplace=True)
Temp_LosAngeles_changed.dropna(subset=['TMAX'], inplace=True)
Temp_LosAngeles_changed.dropna(subset=['TMIN'], inplace=True)

#Temp_SantsBarbara_changed
Temp_SantsBarbara_changed = Temp_SantaBarbara.drop(['STATION', 'NAME'],axis='columns')
Temp_SantsBarbara_changed['AVG'] = (Temp_SantsBarbara_changed['TMAX'] + Temp_SantsBarbara_changed['TMIN']) // 2
Temp_SantsBarbara_changed['TMAX'].replace('', np.nan, inplace=True)
Temp_SantsBarbara_changed['TMIN'].replace('', np.nan, inplace=True)
Temp_SantsBarbara_changed.dropna(subset=['TMAX'], inplace=True)
Temp_SantsBarbara_changed.dropna(subset=['TMIN'], inplace=True)
