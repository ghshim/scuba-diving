import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer

def extract_text(data_path):
    '''
    extract text(abstract) in data
    '''
    df = pd.read_csv('../data/scuba_diving_safety.csv')
    texts = df['abstract'].to_list()
    return texts

def tokenizer(text):
    tokens = RegTok.tokenize(text.lower())
    # stopwords 제외
    words = [word for word in tokens if (word not in english_stops) and len(word)>2]
    # porter stemmer 적용
    features = (list(map(lambda token: PorterStemmer().stem(token), words)))
    return features

def tsne_graph(tsne_2, lim=None):
    x = tsne_2[:, 0]
    y = tsne_2[:, 1]

    plt.figure(figsize=(10, 6))
    tfig = sns.scatterplot(
        x=x, y=y,
        legend="full",
        alpha=0.3
    )

    tsne_fig = tfig.get_figure()
    tsne_fig.savefig('../figure/scuba_diving_safety_tsne.png')

def show_tsne():
    # load data and extract texts (abstract)
    path = '../data/scuba_diving_safety.csv'
    papers = extract_text(path)

    cachedStopWords = stopwords.words("english")
    RegTok = RegexpTokenizer("[\w']{3,}")
    english_stops = set(stopwords.words('english'))

    tfidf = TfidfVectorizer(tokenizer=tokenizer)
    papers_tfidf = tfidf.fit_transform(papers)

    tsne = TSNE(n_components=2, random_state=7)
    tsne_tfidf = tsne.fit_transform(papers_tfidf)
    print('TSNE dimension:', tsne_tfidf.shape)

    tsne_graph(tsne_tfidf)
