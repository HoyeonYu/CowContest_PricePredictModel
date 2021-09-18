# Target
# 독립변수 3번 평균 도체 중량
# Data Source : 소 도축 데이터
# 소의 종류 : 한우
# 육질 등급 : 1등급 이상 (1등급, 1+등급, 1++등급)
# 기간 : 201501 ~ 201912
# 목표 : 해당 기간 내 1등급 이상의 한우 월간 평균 도체 중량 구하기
#
# Column
# 날짜, 도체평균
#
# Process Flow
# 1. 소의 종류 '한우' 이외 제거하기 (육우, 젖소)
# 2. 육질 등급 '1등급' 미만 제거하기
# 3. 평균 도체 중량 X 도축 두수 곱해 전체 도체 중량 구하기 (도축 두수는 그대로 유지)
# 4. 도축년월 같은 것끼리 평균 도체 중량 구하기

import os

import pandas as pd

findWeightDataPath = 'rawData/소도축_2015_2020/소도축_'
saveWeightDataPath = 'preprocessedData/3_cowWeight/'

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


# Flow 2, Filtering Meat Grade
def flow2():
    weightDF = pd.read_csv(saveWeightDataPath + 'flow1.csv', sep=',', encoding='CP949')
    weightDF = weightDF[['도축년월', '육질등급', '평균도체중량', '도축두수']]
    not1stGrade = weightDF[weightDF['육질등급'].str[:1] != '1'].index

    originalLen = len(weightDF)
    dropLen = len(not1stGrade)

    weightDF = weightDF.drop(not1stGrade)
    print('* FLOW 2: Filtering Meat Grade *  %d/%d Dropped' % (dropLen, originalLen))

    weightDF.to_csv(saveWeightDataPath + 'flow2.csv', encoding='cp949')


# Flow 3, Get Total Weight in Same Row
def flow3():
    weightDF = pd.read_csv(saveWeightDataPath + 'flow2.csv', sep=',', encoding='CP949')
    weightDF = weightDF[['도축년월', '평균도체중량', '도축두수']]
    weightDF['총도체중량'] = weightDF['평균도체중량'] * weightDF['도축두수']

    print('* FLOW 3: Get Total Weight in Same Row *')

    weightDF.to_csv(saveWeightDataPath + 'flow3.csv', encoding='cp949')


# Flow 4, Get Average Weight in Same Month
def flow4():
    weightDF = pd.read_csv(saveWeightDataPath + 'flow3.csv', sep=',', encoding='CP949')
    weightDF = weightDF[['도축년월', '총도체중량', '도축두수']]
    weightDF = weightDF.sort_values(by='도축년월')

    weightTotalDF = weightDF['총도체중량'].groupby([weightDF['도축년월']]).sum()
    weightNumDF = weightDF['도축두수'].groupby([weightDF['도축년월']]).sum()
    weightDF = weightTotalDF / weightNumDF
    weightDF = pd.DataFrame(weightDF, columns=['평균도체중량'])

    print('* FLOW 4: Get Average Weight in Same Month *')

    weightDF.to_csv(saveWeightDataPath + 'flow4.csv', encoding='cp949', index=False)


# flow1()
# flow2()
# flow3()
flow4()
