# Target
# 목표 : 독립변수 12개와 종속변수인 생산량과의 상관성 분석
#
# Flow
# 1. 정규분포를 이용해 정규화한 데이터의 상관성 분석
#   1-1. Cluster Map
#   1-2. Heat Map
#
# 2. Min-Max를 이용해 정규화한 데이터의 상관성 분석
#   2-1. Cluster Map
#   2-2. Heat Map

import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, font_manager, rc
import seaborn as sns

np.random.seed(seed=0)
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

normDistriPath = 'preprocessedFinal_Normalized_NormalDistribution.csv'
minMaxPath = 'preprocessedFinal_Normalized_MinMax.csv'
saveFigurePath = 'correlationFigure/'

if not os.path.exists(saveFigurePath):
    os.makedirs(saveFigurePath)

# Flow 1, Find Correlation in Data which is Normalized by using Normal Distribution
normDistriDF = pd.read_csv(normDistriPath, sep=',', encoding='CP949')
normDistriDF = normDistriDF.drop('날짜', axis=1)
normDistriCorr = normDistriDF.corr()

# Flow 1-1, Get Cluster Map (Normal Distribution)
plt.figure(figsize=(12, 12))
clmap = sns.clustermap(normDistriCorr, annot=True, cmap='RdYlBu_r', vmin=-1, vmax=1)
plt.setp(clmap.ax_heatmap.get_xticklabels(), rotation=40, horizontalalignment='right')
plt.savefig(saveFigurePath + 'ClusterMap_NormalDistribution')
plt.close()
print('* FLOW 1-1: Get Cluster Map (Normal Distribution)')

# Flow 1-2, Get Heat Map (Normal Distribution)
plt.figure(figsize=(12, 12))
heatMap = sns.heatmap(normDistriCorr, annot=True, cmap='RdYlBu_r', vmin=-1, vmax=1)
heatMap.set_xticklabels(heatMap.get_xticklabels(), rotation=40, horizontalalignment='right')
plt.savefig(saveFigurePath + 'HeatMap_NormalDistribution')
plt.close()
print('* FLOW 1-2: Get Heat Map (Normal Distribution)')

# Flow 2, Find Correlation in Data which is Normalized by using Min-Max
minMaxDF = pd.read_csv(minMaxPath, sep=',', encoding='CP949')
minMaxDF = minMaxDF.drop('날짜', axis=1)
minMaxCorr = minMaxDF.corr()

# Flow 2-1, Get Cluster Map (Min-Max)
plt.figure(figsize=(12, 12))
clmap = sns.clustermap(minMaxCorr, annot=True, cmap='RdYlBu_r', vmin=-1, vmax=1)
plt.setp(clmap.ax_heatmap.get_xticklabels(), rotation=40, horizontalalignment='right')
plt.savefig(saveFigurePath + 'ClusterMap_MinMax')
plt.close()
print('* FLOW 2-1: Get Cluster Map (Min-Max)')

# Flow 2-2, Get Heat Map (Min-Max)
plt.figure(figsize=(12, 12))
heatMap = sns.heatmap(minMaxCorr, annot=True, cmap='RdYlBu_r', vmin=-1, vmax=1)
heatMap.set_xticklabels(heatMap.get_xticklabels(), rotation=40, horizontalalignment='right')
plt.savefig(saveFigurePath + 'HeatMap_MinMax')
plt.close()
print('* FLOW 2-2: Get Heat Map (Min-Max)')
