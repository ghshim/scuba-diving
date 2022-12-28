"""
주어진 논문을 연도별로 카운트하여 csv 파일에 저장하고 이를 그래프를 그려 저장합니다.

Args:
    -d: data(document) path (required)
    -s: path to save files (required)
    -t: title of figure 

Returns:
    Saved Path: ./data/topic name/ (csv), ./figure/topic name/ (figure)
    Name of files: '/topic' + save_path[-1] + '_YearCount.csv' (csv), '/topic' + save_path[-1] + '_YearCount.png'

    Count given papers by year and store count by year in csv and graph

입력 예시:
    python year_count.py -d './data/topic2/trust_robot.csv' -s '/topic2'
"""

import math
import argparse
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def draw_barplot(x, y, xlabel, ylabel, title=None):
    # save the result of years count in figure 
    plt.figure(figsize=(10, 6))
    plt.rcParams['axes.unicode_minus'] = False
    # if you use MacOS
    plt.rcParams['font.family'] = 'AppleGothic'
    # else if you use Windows
    # plt.rcParams['font.family'] = 'Malgun Gothic'

    fig = sns.barplot(x=x, y=y, color='tab:blue')
    fig.set(xlabel=xlabel, ylabel=ylabel)

    if title is not None:
        fig.set(title=title)

    return fig.get_figure()

    
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
    csv_name = '/topic' + save_path[-1] + "_YearCount.csv"
    fig_name = '/topic' + save_path[-1]  + "_YearCount.png"

    df = pd.read_csv(data_path)

    years = []
    for i in range(len(df['date'])):
        if type(df.loc[i, 'date']) == str:
            years.append(df.loc[i, 'date'].split()[0])
        elif math.isnan(df.loc[i, 'date']):
            years.append('None')
        else:
            print(i, df.loc[i, 'date'])

    # count by years
    df['year'] = years
    years_count = df['year'].value_counts().sort_index()

    # save the result of years count in CSV file
    result = pd.DataFrame()
    result['year'] = np.array(years_count.index)
    result['count'] = years_count.values
    result.to_csv('./data' + save_path + csv_name, index=False)

    # draw figure and save it
    fig = draw_barplot(result['year'][:-2], result['count'][:-2], 'Year', 'Count', title)
    fig.savefig('./figure' + save_path + fig_name)


def count_by_topic():
    csv_name = '/topic' + save_path[-1] + "_TopicCount.csv"
    fig_name = '/topic' + save_path[-1] + "_TopicCount.png"

    df = pd.read_csv('../data/topic2/topic2_predicted.csv')

    total = len(df)
    count_papers = df['predictedTopic'].value_counts().sort_index()
    pct = count_papers / total

    # save results
    result = pd.DataFrame()
    result['topic'] = [i for i in range(0, 10)]
    result['count'] = count_papers
    result['percentage'] = pct
    years_count.to_csv('./data' + save_path + csv_name, header=False)

    # draw figure and save it
    fig = draw_barplot(result['topic'], result['count'], 'Topic', 'Count', title)
    fig.savefig('./figure' + save_path + fig_name)


if __name__ == '__main__':
    global data_path, save_path, title
    parser = argparse.ArgumentParser(description="-d input data path(csv) -s save path to store output -t title of figure")
    parser.add_argument('-d', help="input_data_path", required=True)
    parser.add_argument('-s', help="save_path", required=True)
    parser.add_argument('-t', help="fig_title")
    
    args = parser.parse_args()

    data_path = args.d; save_path = args.s; title = args.t
    print("data_path:", data_path)
    print("save_path:", save_path)
    print("title of figure:", title)
    print()

    years_count(data_path, save_path)
