# Target
# 독립변수 9번 비육우 두당 사육비
# Data Source : 국가 통계 포털 '한우 비육우 두당 사육비'
# 기간 : 2015 ~ 2019
# 목표 : 해당 기간 내 연간 두당 사육비 구하기
#
# Column
# 날짜, 두당 사육비
#
# Process Flow
# 1. 연도별 평균 비용 합계 구하기

import os
import pandas as pd

findCostDataPath = 'rawData/비육우두당사육비_2015_2019/비육우두당사육비_2015_2019.csv'
saveCostDataPath = 'preprocessedData/9_cowBreedingCost/'

if not os.path.exists(saveCostDataPath):
    os.makedirs(saveCostDataPath)


# Flow 1, Get Average Breeding Cost in Same Year
def flow1():
    costDF = pd.read_csv(findCostDataPath, sep=',', encoding='CP949')
    cleanCostDF = pd.DataFrame(columns=['연도', '두당사육비'])
    year, cost = [], []

    for colIdx, col in enumerate(costDF.columns):
        if costDF.iloc[0, colIdx] == '평균':
            year.append(col[:4])
            cost.append(costDF.iloc[1, colIdx])

    cleanCostDF['연도'], cleanCostDF['두당사육비'] = year, cost

    print('* FLOW 1: Get Average Breeding Cost in Same Year *')

    cleanCostDF.to_csv(saveCostDataPath + 'flow1.csv', encoding='cp949')


flow1()
