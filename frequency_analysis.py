import pandas as pd
import seaborn as sns
import csv
from sklearn.feature_extraction.text import TfidfVectorizer

def frequency_analysis(word_token):
    #상위 30개까지만 확인
    n = 30

    frequency_series = pd.Series(word_token).value_counts().head(n)

    frequency_series.to_csv("./data/topic3/topic3_frequency.csv")

    #print(frequency_series)
    return frequency_series

def tfidf_analysis(dataset):
    tfidf = TfidfVectorizer(min_df=3)
    tfidf.fit(dataset)
    feature_names = tfidf.get_feature_names()
    tfidf_matrix = tfidf.transform([dataset[70]]).todense()
    feature_index = tfidf_matrix[0, :].nonzero()[1]
    tfidf_scores = zip([feature_names[i] for i in feature_index], [tfidf_matrix[0, x] for x in feature_index])

    return dict(tfidf_scores)

def show_figure_forFrequency(obj):
    sns.set(rc={'figure.figsize': (30, 15)})
    splot = sns.barplot(y=obj.index, x=obj.values, orient='h', color='tab:blue')
    sfig = splot.get_figure()
    sfig.savefig('../figure/topic3/topic3_users*_Frequency.png')

def show_figure_forTfidf(n, obj):
    sns.set(rc={'figure.figsize': (30, 15)})
    splot = sns.barplot(y=obj.index, x=obj.values, orient='h')
    sfig = splot.get_figure()

    sfig.savefig('../figure/scuba_diving_safety_tfidf.png')