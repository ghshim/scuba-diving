import math
import argparse
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def years_count(data_path, save_path='./'):
    '''
    전체 데이터의 개수와 데이터를 연도별로 분류하여 각 연도별 데이터의 개수를 dictionary로 리턴
    또한, 연도별 논문의 수를 csv로 변환 및 막대 그래프로 나타낸 후 dir folder에 저장 (x축: 연도, y축: 연도별 데이터 개수)
    
    input
      data_path: path of data
      save_path: directory name to save files
    output
      total_num: 전체 데이터 개수
      data_year: 연도를 key로 가지며 해당 년도의 데이터를 value로 가짐
    '''
    csv_name = "/YearCount.csv"
    fig_name = "/YearCount.png"

    df = pd.read_csv(data_path)
    
    years = []
    for i in range(len(df['date'])):
        if type(df.loc[i, 'date']) == str:
            years.append(df.loc[i, 'date'].split()[0])
        elif math.isnan(df.loc[i, 'date']):
            years.append('None')
        else:
            print(i, df.loc[i, 'date'])

    # save the result of years count in CSV file
    df['year'] = years
    years_count = df['year'].value_counts().sort_index()
    years_count.to_csv('./figure' + save_path + csv_name, header=False)

    # save the result of years count in figure 
    plt.figure(figsize=(10, 6))
    plt.rcParams['axes.unicode_minus'] = False
    # if you use MacOS
    plt.rcParams['font.family'] = 'AppleGothic'
    # else if you use Windows
    # plt.rcParams['font.family'] = 'Malgun Gothic'

    fig = sns.barplot(x=years_count.index, y=years_count.values, color='tab:blue')
    fig.set(title=title, xlabel='Year', ylabel='Count')
    fig = fig.get_figure()
    fig.savefig('./figure' + save_path + fig_name)

if __name__ == '__main__':
    global data_path, save_path, title
    parser = argparse.ArgumentParser(description="-d input data path(csv) -s save path to store output -t title of figure")
    parser.add_argument('-d', help="input_data_path", required=True)
    parser.add_argument('-s', help="save_path", required=True)
    parser.add_argument('-t', help="fig_title", required=True)
    
    args = parser.parse_args()

    data_path = args.d; save_path = args.s; title = args.t
    print("data_path:", data_path)
    print("save_path:", save_path)
    print("title of figure:", title)
    print()

    years_count(data_path, save_path)
