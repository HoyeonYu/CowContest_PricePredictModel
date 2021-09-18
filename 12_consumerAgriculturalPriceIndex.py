# Target
# 독립변수 12번 소비자 물가 지수 (농축수산물 지수)
# Data Source : 국가 통계 포털 '품목성질별 소비자물가지수'
# 기간 : 2015 ~ 2019
# 목표 : 해당 기간 내 소비자 물가 지수 구하기 (농축수산물 지수)
#
# Column
# 연월, 물가농축수산물지수
#
# Process Flow
# 1. 해당 기간 내 월간 소비자 물가 지수 구하기 (농축수산물 지수)

import os
import pandas as pd

findTotalDataPath = 'rawData/소비자물가지수_2015_2019/소비자물가지수_2015_2019.csv'
saveTotalDataPath = 'preprocessedData/12_consumerAgriculturalPriceIndex/'

if not os.path.exists(saveTotalDataPath):
    os.makedirs(saveTotalDataPath)


# Flow 1, Get Consumer Total Price Index in Same Month
def flow1():
    totalPriceDF = pd.read_csv(findTotalDataPath, sep=',', encoding='CP949')
    cleanTotalPriceDF = pd.DataFrame(columns=['연월', '물가농축수산물지수'])
    month, totalPrice = [], []

    for colIdx, col in enumerate(totalPriceDF.columns[2:]):
        month.append(col[:4] + col[6:8])
        totalPrice.append(totalPriceDF.iloc[2, colIdx + 2])

    cleanTotalPriceDF['연월'], cleanTotalPriceDF['물가농축수산물지수'] = month, totalPrice

    print('* FLOW 1: Get Consumer Total Price Index in Same Month *')

    cleanTotalPriceDF.to_csv(saveTotalDataPath + 'flow1.csv', encoding='cp949', index=False)


flow1()
