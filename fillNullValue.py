# Target
# 문제 상황 : 암송아지, 수송아지 가격의 약 40%가 결측값
# 목표 : 암송아지, 수송아지 결측값 채우기
#
# Flow
# 1. 결측값 (-) 나오기 전 값과 나온 후 값 기준으로 선형 보간

import os

import numpy as np
import pandas as pd
import math

dataPath = 'preprocessed_Merged.csv'
savePath = 'preprocessed_FillNull.csv'
missingDF = pd.read_csv(dataPath, sep=',', encoding='CP949')

missingIdxList = []
isInterpolate = False

for rowIdx in range(len(missingDF)):
    print(missingDF.iloc[rowIdx, [3]].item(), missingDF.iloc[rowIdx, [4]].item())

    if missingDF.iloc[rowIdx, [3]].item() == '-' or math.isnan(float(missingDF.iloc[rowIdx, [3]].item())):
        missingIdxList.append(rowIdx)
        isInterpolate = False

    else:
        if len(missingIdxList) > 0:
            isInterpolate = True

    if rowIdx == len(missingDF) - 1 and len(missingIdxList) > 0:
        isInterpolate = True

    if isInterpolate:
        firstIdx = missingIdxList[0] - 1
        lastIdx = missingIdxList[len(missingIdxList) - 1] + 1

        if firstIdx < 0:
            firstIdx = lastIdx
        if lastIdx > len(missingDF) - 1:
            lastIdx = firstIdx

        prevFemaleVal = float(missingDF.iloc[firstIdx, [3]].item())
        nextFemaleVal = float(missingDF.iloc[lastIdx, [3]].item())

        prevMaleVal = float(missingDF.iloc[firstIdx, [4]].item())
        nextMaleVal = float(missingDF.iloc[lastIdx, [4]].item())

        for idx, missingRow in enumerate(missingIdxList):
            ratio = (idx + 1) / (len(missingIdxList) + 1)
            missingDF.iloc[missingRow, 3] = (prevFemaleVal * (1 - ratio)) + (nextFemaleVal * ratio)
            missingDF.iloc[missingRow, 4] = (prevMaleVal * (1 - ratio)) + (nextMaleVal * ratio)

        missingIdxList = []
        isInterpolate = False

missingDF.to_csv(savePath, encoding='cp949', index=False)
