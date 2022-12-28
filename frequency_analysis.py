
"""
주어진 문서에 대해 키워드 빈도수 분석을 실시한 후, 빈도수가 높은 30개의 keyword를 선정하여 해당 단어와 점수를 csv파일로 저장합니다.
   
Args:
    -d: data(document) path (required)
    -s: path to save t-SNE graph (required)

Returns: 
    Saved Path: ./data/topic name/
    Name of graph: '/topic' + save_path[-1] + '_frequency.csv'

    CSV file which stores top 30 keywords selected by frequency analysis and the count for each keyword

입력 예시:
    python frequency_analysis.py -d './data/topic2/trust_robot.csv' -s '/topic2'
"""

import sys
import itertools
import argparse
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

sys.path.insert(0, '../')
import preprocess_csv as preprocess


def merge_dicts(a, b):
    c = a.copy()  # a 변수를 c에 copy 한 후
    c.update(b)   # c를 update하여 반환
    return c    


def tokenizer(text):
    '''
    apply tokenizer
    '''
    cachedStopWords = stopwords.words("english")
    RegTok = RegexpTokenizer("[\w']{3,}")
    english_stops = set(stopwords.words('english'))
    tokens = RegTok.tokenize(text.lower())
    # stopwords 제외
    words = [word for word in tokens if (word not in english_stops) and len(word) > 2]
    
    stemmer = PorterStemmer()
    word_token = [stemmer.stem(i) for i in words]
    
    return word_token



def get_token2word_dict(papers):
    '''
    return the list of dictionary (key: stemmized token, value: original word)
    '''
    word_token_list = []
    for text in papers:
        cachedStopWords = stopwords.words("english")
        RegTok = RegexpTokenizer("[\w']{3,}")
        english_stops = set(stopwords.words('english'))
        tokens = RegTok.tokenize(text.lower())
        # stopwords 제외
         # stopwords 제외
        words = [word for word in tokens if (word not in english_stops) and len(word) > 2]

        stemmer = PorterStemmer()
        word_token_dict = [{stemmer.stem(word):word} for word in words]
        word_token_list.append(word_token_dict)
        
    # flatten
    word_token_list = list(itertools.chain(*word_token_list))
    
    word_token_dict = dict()
    for element in word_token_list:
        word_token_dict = merge_dicts(word_token_dict, element)
    
    return word_token_dict


def frequency_analysis(word_token, top_n=30):
    frequency_series = pd.Series(word_token).value_counts().head(top_n)
    return frequency_series


def get_frequency(data_path, save_path):
    filename = '/topic' + save_path[-1] + '_frequency.csv'
    # lemmatizer for lemmatization
    lemmatizer = WordNetLemmatizer()

    # extract texts (abstracts)
    df = pd.read_csv(data_path)
    papers = preprocess.extract_text(df)
    word_token = [tokenizer(paper) for paper in papers]
    word_token = list(itertools.chain(*word_token))
    
    # get frequency
    frequency_series = frequency_analysis(word_token)
    fq = pd.DataFrame()
    fq['keyword'] = np.array(frequency_series.index)
    fq['count'] = frequency_series.values
    
    # get origin word
    word_token_dict = get_token2word_dict(papers)
    
    # convert to df and save it in the csv format
    keywords = fq['keyword']
    lemma_keywords = [lemmatizer.lemmatize(word_token_dict[keyword], pos='v') for keyword in keywords]

    fq_df = pd.DataFrame()
    fq_df['keyword'] = lemma_keywords; fq_df['count'] = fq['count']

    fq_df.to_csv('./data' + save_path + filename, index=False)


def main():
    get_frequency(data_path, save_path)


if __name__ == '__main__':
    global data_path, save_path

    parser = argparse.ArgumentParser(description="-d input data path(csv) -s save path to store output -t title of figure -tx textrank csv path -fq frequency csv path")
    parser.add_argument('-d', help="input_data_path", required=True)
    parser.add_argument('-s', help="save_path", required=True)
    
    args = parser.parse_args()

    data_path = args.d; save_path = args.s
    print("data_path:", data_path)
    print("save_path:", save_path) 
  
    main()