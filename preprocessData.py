import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

np.random.seed(seed=0)
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

butcher_read_list = []
for year in range(4):
    butcher_read_list.append('D:/study/python/CowContest/rawData/소도축_2015_2018/소도축_' + str(2015 + year) + '.csv')

breed_read_list = []
for year in range(1):
    breed_quarter_list = []
    for quarter in range(4):
        breed_quarter_list.append('D:/study/python/CowContest/rawData/소사육_2018_2018/'
                                  '분기별 소사육/소사육_' + str(2018 + year) + '_' + str(quarter + 1) + 'q.csv')
    breed_read_list.append(breed_quarter_list)

birth_read_list = []
for year in range(4):
    birth_read_list.append('D:/study/python/CowContest/rawData/소출생_2015_2018/소출생_' + str(2015 + year) + '.csv')

butcher_save = 'D:/study/python/CowContest/preprocessedData/preprocessed_소도축.csv'
butcher_df = pd.read_csv(butcher_read_list[0], nrows=0, encoding='cp949')

# Analyze Butcher Data and Drop Unnecessary Data, Convert Month to Quarter
for year in range(len(butcher_read_list)):
    print('======================================================')
    print('butcher_read_list -> ', butcher_read_list[year], '\n')
    data = pd.read_csv(butcher_read_list[year], nrows=1000000, encoding='cp949')
    print('Initial,\tLength:', (len(data)))

    data = data[['시도명', '시군명', '소의종류', '소의성별', '도축개월령', '도축년월', '육질등급', '평균도체중량', '도축두수']]

    data.dropna(axis=0, inplace=True)
    print('After Drop Null,\tLength: ', len(data))

    # plt.figure(figsize=(7, 7))
    # plt.title(str(2015 + year) + '년도 소도축 소 종류', fontsize=30)
    # data['소의종류'].value_counts().plot.pie(autopct='%.2f%%', textprops={'fontsize': 20, 'weight': 'bold'})
    # plt.show()

    data = data[data['소의종류'] == '한우']
    print('After Drop Except K-Cow,\tLength: ', len(data))

    # plt.figure(figsize=(7, 7))
    # plt.title(str(2015 + year) + '년도 소도축 소 성별', fontsize=30)
    # data['소의성별'].value_counts().plot.pie(autopct='%.2f%%', textprops={'fontsize': 20, 'weight': 'bold'})
    # plt.show()

    data = data[data['소의성별'] != '기타(프리마틴 등)']
    data = data[data['육질등급'] != '알수없음']
    print('After Drop ETC,\tLength: ', len(data))

    # plt.figure(figsize=(7, 7))
    # plt.title(str(2015 + year) + '년도 소도축 연월', fontsize=30)
    # data['도축년월'].value_counts().plot.pie(autopct='%.2f%%', textprops={'fontsize': 20, 'weight': 'bold'})
    # plt.show()

    for idx in range(len(data)):
        data['도축년월'].iloc[idx] = (2015 + year) * 100 + ((data['도축년월'].iloc[idx] % 100) + 2) // 3

    # plt.figure(figsize=(7, 7))
    # plt.title(str(2015 + year) + '년도 소도축 분기', fontsize=30)
    # data['도축년월'].value_counts().plot.pie(autopct='%.2f%%', textprops={'fontsize': 20, 'weight': 'bold'})
    # plt.show()

    print(data.head())
    butcher_df = pd.concat([butcher_df, data])
    print('======================================================\n')

print(butcher_df.head())
butcher_df.to_csv(butcher_save, encoding='cp949')
