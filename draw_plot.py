"""
빈도수 분석 및 Text Rank 분석으로 선정된 top 30개의 키워드를 bar plot으로 표현하여 저장합니다.

Args:
    -d: data(document) path (required)
    -s: path to save bar plot
    -t: title of figure 
    -tx: path of textrank csv file (required)
    -fq: path of frequency analysis csv file (required)

Returns: 
    Saved Path: ./figure/topic name/
    Name of graph: '/topic' + save_path[-1] + '_frequency.png' (frequency analysis)
                   '/topic' + save_path[-1] + '_TextRank.png'  (TextRank)

    bar plot that shows top 30 keywords selected by frequency analysis and TextRank and count for each keyword.

입력 예시:
    python draw_plot.py -d './data/topic2/trust_robot.csv' -s '/topic2' -tx './data/topic2/topic2_Textrank.csv' -fq './data/topic2/topic2_frequency.csv'
"""

import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show_figure(x, y, xlabel, ylabel, save_path):
    sns.set(rc={'figure.figsize': (25, 30)}) #, 'axes.labelsize':25})
    splot = sns.barplot(x=x, y=y, color='tab:blue', orient='h')
    
    splot.set_xlabel(xlabel, size=25)
    splot.set_ylabel(ylabel, size=25)
    
    x_ticks = [int(i) for i in splot.get_xticks()]
    splot.set_xticklabels(x_ticks, size=25)
    splot.set_yticklabels([i for i in y], size=25)
    
    splot.invert_yaxis()
    sfig = splot.get_figure()
    sfig.savefig(save_path)


def main():
    fq_save_path = './figure' + save_path + save_path + '_frequency.png'
    tr_save_path = './figure' + save_path + save_path + '_TextRank.png'
    
    # draw plot for frequency analysis
    xlabel = 'Count'; ylabel = 'Keyword'
    fq_df = pd.read_csv(fq_path)
    fq_df = fq_df.sort_values(by=['count'], ascending=True)
    show_figure(fq_df['count'].values, fq_df['keyword'].values,xlabel, ylabel, fq_save_path)

    # draw plot for Text Rank
    xlabel = 'Rank'; ylabel = 'Keyword'
    tr_df = pd.read_csv(tr_path)
    tr_df = tr_df.sort_values(by=['rank'], ascending=True)
    show_figure(tr_df['rank'].values, tr_df['keyword'].values,xlabel, ylabel, tr_save_path)


if __name__ == '__main__':
    global data_path, save_path, title, tr_path, fq_path

    parser = argparse.ArgumentParser(description="-d input data path(csv) -s save path to store output -t title of figure -tx textrank csv path -fq frequency csv path")
    parser.add_argument('-d', help="input_data_path", required=True)
    parser.add_argument('-s', help="save_path", required=True)
    parser.add_argument('-t', help="fig_title")
    parser.add_argument('-tx', help="textrank_path", required=True)
    parser.add_argument('-fq', help="frequency_path", required=True)
    
    args = parser.parse_args()

    data_path = args.d; save_path = args.s; title = args.t; tr_path = args.tx; fq_path = args.fq
    print("data_path:", data_path)
    print("title of figure:", title)
    print("tr_path:", tr_path)
    print("fq_path:", fq_path)
    print()

    main()