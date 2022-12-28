"""
Topic Modeling을 통해 분류된 topic 별 데이터의 개수를 카운트하여 이를 csv 파일로 저장하고 그래프로 표현하여 저장합니다.
본 프로젝트의 topic_modelng.py을 활용하여 topic modeling을 한 경우, 'topicname_predicted.csv'에 그 결과가 저장됩니다. 

Args:
    -d: data(document) path (required)
    -s: path to save t-SNE graph (required)
    -t: title of figure 

Returns:
    Saved Path: ./data/topic name/ (csv), ./figure/topic name/ (figure)
    Name of files: '/topic' + save_path[-1] + '_TopicCount.csv' (csv), '/topic' + save_path[-1] + '_TopicCount.png'

    Count given papers by year and store count by year in csv and graph

입력 예시:
    python topic_count.py -d './data/topic2/topic2_predicted.csv' -s '/topic2' 
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


def count_by_topic(data_path, save_path):
    csv_name = '/topic' + save_path[-1] + "_TopicCount.csv"
    fig_name = '/topic' + save_path[-1] + "_TopicCount.png"

    df = pd.read_csv(data_path)

    total = len(df)
    count_papers = df['predictedTopic'].value_counts().sort_index()
    topics = np.array(count_papers.index) + 1
    pct = count_papers / total

    # save results
    result = pd.DataFrame()
    result['topic'] = topics
    result['count'] = count_papers
    result['percentage'] = pct
    result.to_csv('./data' + save_path + csv_name, index=False)

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

    count_by_topic(data_path, save_path)
