# Target
# 목표 : 기존의 일간으로 통합된 데이터와 월간 / 연간으로 흩어진 데이터 합치기
#
# Flow
# 1. 3, 6, 8, 9, 10, 11, 12 데이터 리스트로 저장
# 2. 데이터 개수 60개일 경우 월간 데이터로 판별 (12개월 X 5년), 아니면 연간 데이터
# 3. 월간일 경우 기존 일간 데이터의 같은 월로 중복 삽입
# 4. 연간일 경우 기존 일간 데이터의 같은 연도로 중복 삽입

import os

import numpy as np
import pandas as pd

dataPath = 'preprocessedDataList'
dailyDataPath = 'dailyData.csv'
savePath = 'preprocessed_Merged.csv'
dailyDF = pd.read_csv(dailyDataPath, sep=',', encoding='CP949')

for data_idx, data in enumerate(os.listdir(dataPath)):
    dataDF = pd.read_csv(dataPath + '/' + data, sep=',', encoding='CP949')
    dataDateList, dataValList = [], []
    isMonthly = (len(dataDF) == 60)

    for rowIdx in range(len(dataDF)):
        dataDateList.append(dataDF.iloc[rowIdx, [0]].item())
        dataValList.append(dataDF.iloc[rowIdx, [1]].item())

    dataListIdx = 0
    convertDailyList = []

    for rowIdx in range(len(dailyDF)):
        if isMonthly:
            if dailyDF.iloc[rowIdx, [0]].item() // 100 != dataDateList[dataListIdx]:
                dataListIdx += 1
        else:
            if dailyDF.iloc[rowIdx, [0]].item() // 10000 != dataDateList[dataListIdx]:
                dataListIdx += 1

        convertDailyList.append(dataValList[dataListIdx])

    convertDailyDF = pd.DataFrame(columns=[dataDF.columns[1]])
    convertDailyDF[dataDF.columns[1]] = convertDailyList
    dailyDF = pd.concat([dailyDF, convertDailyDF], axis=1)

    print('* Data %s: %s,\tShape %d X %d *' % (data, dataDF.columns[1], dailyDF.shape[0], dailyDF.shape[1]))

    dailyDF.to_csv(savePath, encoding='cp949', index=False)
