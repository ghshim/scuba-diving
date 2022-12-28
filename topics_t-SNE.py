"""
빈도수 분석 및 Text Rank 분석으로 선정된 top 30개의 키워드를 벡터로 변환한 후, 이 키워드들에 대한 벡터를 t-SNE 그래프로 표현하여 'figure' 폴더에 저장합니다. 
   
Args:
    -d: data(document) path (required)
    -s: path to save t-SNE graph (required)
    -t: title of figure 

Returns: 
    Saved Path: ./figure/topic name/
    Name of graph: '/topic' + save_path[-1] + '_topics_t-SNE.png'

    t-SNE graph that shows the distribution of detailed topics classified by topic modeling. 
    Can understand the relationship between detailed topics.

입력 예시:
    python topics_t-SNE.py -d './data/topic2/topic2_predicted.csv' -s '/topic2'
"""

import sys
import argparse
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer

import preprocess_csv as preprocess

def tokenizer(text):
    # token화
    RegTok = RegexpTokenizer("[\w']{3,}")
    tokens = RegTok.tokenize(text.lower())
    # stopwords 제외
    cachedStopWords = stopwords.words("english")
    english_stops = set(stopwords.words('english'))
    words = [word for word in tokens if (word not in english_stops) and len(word)>2]
    # porter stemmer 적용
    features = (list(map(lambda token: PorterStemmer().stem(token), words)))
    return features


def tsne_graph(tsne_2, lim=None):
    filename = '/topic' + save_path[-1] + '_t-SNE.png'
    x = tsne_2[:, 0]
    y = tsne_2[:, 1]

    # 한글 깨짐
    plt.figure(figsize=(10, 6))
    plt.rcParams['axes.unicode_minus'] = False
    # if you use MacOS
    plt.rcParams['font.family'] = 'AppleGothic'
    # else if you use Windows
    # plt.rcParams['font.family'] = 'Malgun Gothic'

    tfig = sns.scatterplot(
        x=x, y=y,
        legend="full",
        alpha=0.3
    )
    tfig.set(title=title)
    
    tsne_fig = tfig.get_figure()
    tsne_fig.savefig('./figure' + save_path + filename)



def tsne_graph_target(tsne_2, lim=None):
    filename = '/topic' + save_path[-1] + '_t-SNE.png'

    df = pd.read_csv('./data'+ save_path+ save_path+'_predicted.csv')
    label = df['predictedTopic']
    tsne_df2 = pd.DataFrame({'x': tsne_2[:, 0], 'y':tsne_2[:, 1], 'predicted topic':label})

    # draw t-SNE graph
    plt.figure(figsize=(14, 8))

    # 한글 깨짐
    plt.rcParams['axes.unicode_minus'] = False
    # if you use MacOS
    plt.rcParams['font.family'] = 'AppleGothic'
    # else if you use Windows
    # plt.rcParams['font.family'] = 'Malgun Gothic'
    
    tfig = sns.scatterplot(
        x = 'x', y = 'y',
        hue = 'predicted topic',
        data = tsne_df2,
        palette='muted',
        alpha = 0.7
    )
    plt.legend(title='Predicted Topic', labels = [i for i in range(1, 11)],loc = 2, bbox_to_anchor = (1,1))
    tfig.set(xlabel='X', ylabel='Y')

    if title is not None:
        tfig.set(title=title)

    # save figure
    tsne_fig = tfig.get_figure()
    tsne_fig.savefig('./figure' + save_path + filename)



def show_tsne(data_path, save_path='./', n_components=2):
    df = pd.read_csv(data_path)
    papers = preprocess.extract_text(df)

    tfidf = TfidfVectorizer(tokenizer=tokenizer)
    papers_tfidf = tfidf.fit_transform(papers)
    
    tsne = TSNE(n_components=n_components, perplexity=30.0, n_iter=5000, random_state=7)
    tsne_tfidf = tsne.fit_transform(papers_tfidf)
    print('TSNE dimension:', tsne_tfidf.shape)

    # tsne_graph(tsne_tfidf)
    tsne_graph_target(tsne_tfidf)


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

    show_tsne(data_path)