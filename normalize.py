# Target
# 문제 상황 : 데이터의 범위 매우 다양
# 목표 : 정규분포, Min-Max를 이용한 데이터 정규화
#
# Flow
# 1. 정규분포를 이용한 데이터 정규화
# 2. Min-Max를 이용한 데이터 정규화

import os

import numpy as np
import pandas as pd

dataPath = 'preprocessed_FillNull.csv'
saveNormDistriPath = 'preprocessed_Normalized_NormalDistribution.csv'
saveMinMaxPath = 'preprocessed_Normalized_MinMax.csv'
dataDF = pd.read_csv(dataPath, sep=',', encoding='CP949')

# Flow 1, Normalize by using Normal Distribution
normDistriDF = (dataDF - dataDF.mean()) / dataDF.std()
normDistriDF['날짜'] = dataDF['날짜']
normDistriDF.to_csv(saveNormDistriPath, encoding='cp949', index=False)
print('* FLOW 1: Normalize by using Normal Distribution *')

# Flow 2, Normalize by using Min-Max
minMaxDF = (dataDF - dataDF.min()) / (dataDF.max() - dataDF.min())
minMaxDF['날짜'] = dataDF['날짜']
minMaxDF.to_csv(saveMinMaxPath, encoding='cp949', index=False)
print('* FLOW 2: Normalize by using Min-Max *')

