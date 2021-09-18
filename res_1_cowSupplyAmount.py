# Target
# 종속변수 1번 쇠고기 생산량
# Data Source : KREI 한육우 수급 동향과 전망
# 기간 : 2016 ~ 2020
# 목표 : 생산량 저장
#
# Column
# 연도, 생산량
#
# Process Flow
# 1. 해당 연도 생산량 CSV 저장

import os
import pandas as pd

saveSupplyPath = 'preprocessedData/res_1_cowSupplyAmount/'

if not os.path.exists(saveSupplyPath):
    os.makedirs(saveSupplyPath)


# Flow 1, Save Supply Amount in CSV File
def flow1():
    year = [2016, 2017, 2018, 2019, 2020]
    supply = [231, 239, 236, 245, 249]

    supplyDF = pd.DataFrame(columns=['연도', '생산량'])
    supplyDF['연도'], supplyDF['생산량'] = year, supply

    print('* FLOW 1: Save Supply Amount in CSV File *')

    supplyDF.to_csv(saveSupplyPath + 'flow1.csv', encoding='cp949', index=False)


flow1()
