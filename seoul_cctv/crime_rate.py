import pandas as pd
import googlemaps
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from sklearn  import preprocessing

ctx = '../data/'
df_crime_police = pd.read_csv(ctx+'crime_police.csv'
                              , sep=','
                              , encoding='UTF-8')


df_police = pd.pivot_table(df_crime_police
                          , index='구별'
                          ,aggfunc= np.sum)
# aggfunc 은 평균값 리턴


df_police['강간검거율'] = df_police['강간 검거'] / df_police['강간 발생'] * 100
df_police['강도검거율'] = df_police['강도 검거'] / df_police['강도 발생'] * 100
df_police['살인검거율'] = df_police['살인 검거'] / df_police['살인 발생'] * 100
df_police['절도검거율'] = df_police['절도 검거'] / df_police['절도 발생'] * 100
df_police['폭력검거율'] = df_police['폭력 검거'] / df_police['폭력 발생'] * 100



df_police.drop(['강간 검거','강도 검거','살인 검거','절도 검거','폭력 검거'],1)



# 검거율이 100이 넘는 것은 100으로 정정

ls_rate = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
for i in ls_rate:
    df_police.loc[df_police[i] > 100, i] = 100

print(df_police)


df_police.rename(columns = {'강간 발생':'강간'
                            ,'강도 발생':'강도'
                            ,'살인 발생':'살인'
                            ,'절도 발생':'절도'
                            ,'폭력 발생':'폭력'}
                 ,inplace=True)

ls_crime = ['강간','강도','살인','절도','폭력']

x = df_police[ls_crime].values
min_max_scalar = preprocessing.MinMaxScaler()

"""
스케일링은 선형변환을 적용하여 전체 자료의 분포를
평균 0, 분산 1이 되도록 만드는 과정
"""







