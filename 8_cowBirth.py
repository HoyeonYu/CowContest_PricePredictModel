# Target
# 독립변수 8번 출생 수
# Data Source : 소 출생 데이터
# 소의 종류 : 한우
# 기간 : 201501 ~ 201912
# 목표 : 해당 기간 내 월간 출생 두수 구하기
#
# Column
# 날짜, 출생두수
#
# Process Flow
# 1. 소의 종류 '한우' 이외 제거하기 (육우, 젖소)
# 2. 출생년월 같은 것끼리 출생 두수 구하기

import os
import pandas as pd

findWeightDataPath = 'rawData/소출생_2015_2020/소출생_'
saveWeightDataPath = 'preprocessedData/8_cowBirth/'

if not os.path.exists(saveWeightDataPath):
    os.makedirs(saveWeightDataPath)


# Flow 1, Filtering Cow Type
def flow1():
    concatWeightDF = pd.DataFrame(columns=['소의종류', '출생년월', '출생두수'])

    for i in range(5):  # 2015, 2016, 2017, 2018, 2019 (5)
        year = 2015 + i
        weightDF = pd.read_csv(findWeightDataPath + '%s.csv' % year, sep=',', encoding='CP949')
        weightDF = weightDF[['소의종류', '출생년월', '출생두수']]
        notHanwoo = weightDF[weightDF['소의종류'] != '한우'].index

        originalLen = len(weightDF)
        dropLen = len(notHanwoo)

        weightDF = weightDF.drop(notHanwoo)
        concatWeightDF = pd.concat([concatWeightDF, weightDF])
        print('* FLOW 1: Filtering Cow Type * %s %d/%d Dropped' % (year, dropLen, originalLen))

    concatWeightDF.to_csv(saveWeightDataPath + 'flow1.csv', encoding='cp949')


flow1()
