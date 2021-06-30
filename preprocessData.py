import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

np.random.seed(seed=0)
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

butcher_read_list = []
for year in range(6):
    butcher_read_list.append('D:/study/python/CowContest/rawData/소도축_2015_2020/소도축_' + str(2015 + year) + '.csv')

breed_read_list = []
for year in range(3):
    breed_quarter_list = []
    for quarter in range(4):
        breed_quarter_list.append('D:/study/python/CowContest/rawData/소사육_2018_2020/'
                                  '분기별 소사육/소사육_' + str(2015 + year) + '_' + str(quarter + 1) + 'q.csv')
    breed_read_list.append(breed_quarter_list)

birth_read_list = []
for year in range(6):
    birth_read_list.append('D:/study/python/CowContest/rawData/소출생_2015_2020/소출생_' + str(2015 + year) + '.csv')

csv_save_list = ['D:/study/python/UROP/preprocessing/preprocessed_naverNews.csv',
                 'D:/study/python/UROP/preprocessing/preprocessed_ruliWeb.csv',
                 'D:/study/python/UROP/preprocessing/preprocessed_natePann.csv',
                 'D:/study/python/UROP/preprocessing/preprocessed_kidsBook.csv',
                 'D:/study/python/UROP/preprocessing/preprocessed_kidsSong.csv']

for idx in range(len(butcher_read_list)):
    print('======================================================')
    print('butcher_read_list -> ', butcher_read_list[idx], '\n')
    data = pd.read_csv(butcher_read_list[idx], nrows=1000000, encoding='cp949')
    print('Initial,\tLength:', (len(data)))

    data = data[['시도명', '시군명', '소의종류', '소의성별', '도축개월령', '도축년월', '육질등급', '평균도체중량', '도축두수']]

    data.dropna(axis=0, inplace=True)
    print('After Drop Null,\tLength: ', len(data))

    print(data['소의종류'].value_counts())
    print(data['소의성별'].value_counts())

    plt.figure(figsize=(7, 7))
    plt.title(str(2015 + idx) + '년도 소도축 데이터')
    plt.ylabel('소의 종류')
    data['소의종류'].value_counts().plot.pie(autopct='%.2f%%')
    plt.show()

    print('======================================================\n')
