# Target
# 독립변수 3번 평균 도체 중량
# Data Source : 소 도축 데이터
# 소의 종류 : 한우
# 육질 등급 : 1등급 이상 (1등급, 1+등급, 1++등급)
# 기간 : 201501 ~ 201912
# 목표 : 해당 기간 내 1등급 이상의 한우 일간 도체 평균 구하기
#
# Column
# 날짜, 도체평균
#
# Process Flow
# 1. 소의 종류 '한우' 이외 제거하기 (육우, 젖소)
# 2. 육질 등급 '1등급' 미만 제거하기
# 3. 평균 도체 중량 X 도축 두수 곱해 전체 도체 중량 구하기 (도축 두수는 그대로 유지)
# 4. 도축년월 같은 것끼리 전체 도체 중량 합하기
# 5. 도축 두수대로 나눠 평균 도체 중량 구하기
# 6. 월간을 일간으로 적용
# 7. 날짜, 도체평균만 남기고 나머지 열 제거하기

import os

import pandas as pd

findWeightDataPath = 'rawData/소도축_2015_2020/소도축_'
saveWeightDataPath = 'preprocessedData/3_CowWeight/'

if not os.path.exists(saveWeightDataPath):
    os.makedirs(saveWeightDataPath)


# Flow 1, Filtering Cow Type
def flow1():
    concatWeightDF = pd.DataFrame(columns=['소의종류', '도축년월', '육질등급', '평균도체중량', '도축두수'])

    for i in range(5):  # 2015, 2016, 2017, 2018, 2019 (5)
        year = 2015 + i
        weightDF = pd.read_csv(findWeightDataPath + '%s.csv' % year, sep=',', encoding='CP949')
        weightDF = weightDF[['소의종류', '도축년월', '육질등급', '평균도체중량', '도축두수']]
        notHanwoo = weightDF[weightDF['소의종류'] != '한우'].index

        originalLen = len(weightDF)
        dropLen = len(notHanwoo)

        weightDF = weightDF.drop(notHanwoo)
        concatWeightDF = pd.concat([concatWeightDF, weightDF])
        print('* FLOW 1: Filtering Cow Type * %s %d/%d Dropped' % (year, dropLen, originalLen))

    concatWeightDF.to_csv(saveWeightDataPath + 'flow1.csv', encoding='cp949')


flow1()
