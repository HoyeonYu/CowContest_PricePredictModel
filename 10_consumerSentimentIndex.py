# Target
# 독립변수 10번 소비자 심리 지수
# Data Source : 국가 통계 포털 '한우 비육우 두당 사육비'
# 기간 : 2015 ~ 2019
# 목표 : 해당 기간 내 소비자 심리 지수 구하기
#
# Column
# 연월, 소비자 심리 지수
#
# Process Flow
# 1. 해당 기간 내 월간 소비자 심리 지수 구하기

import os
import pandas as pd

findSentimentDataPath = 'rawData/소비자심리지수_2015_2020/소비자심리지수_2015_2020.csv'
saveSentimentDataPath = 'preprocessedData/10_consumerSentimentIndex/'

if not os.path.exists(saveSentimentDataPath):
    os.makedirs(saveSentimentDataPath)


# Flow 1, Get Consumer Sentiment Index in Same Month
def flow1():
    sentimentDF = pd.read_csv(findSentimentDataPath, sep=',', encoding='CP949')
    sentimentDF = sentimentDF[['연월', '심리지수']]
    notInPeriod = sentimentDF[sentimentDF['연월'] // 100 == 2020].index
    print(notInPeriod)

    sentimentDF = sentimentDF.drop(notInPeriod)
    print('* FLOW 1: Get Consumer Sentiment Index in Same Month *')

    sentimentDF.to_csv(saveSentimentDataPath + 'flow1.csv', encoding='cp949')


flow1()
