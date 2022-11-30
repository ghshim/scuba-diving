import sys
import itertools
import argparse
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

import preprocess_csv as preprocess
from textrank.textrank import KeywordSummarizer


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


def textrank(data_path):
    filename = '/topic' + save_path[-1] + '_TextRank.csv'
    # summarizer for text rank
    summarizer = KeywordSummarizer(tokenize=tokenizer, min_count=2, min_cooccurrence=1)
    # lemmatizer for lemmatization
    lemmatizer = WordNetLemmatizer()

    # extract texts (abstracts)
    df = pd.read_csv(data_path)
    papers = preprocess.extract_text(df)
    word_token_dict = get_token2word_dict(papers)

    # text rank... extract keywords in abstracts
    textrank_result = summarizer.summarize(papers, topk=30)

    # convert to df and save it in the csv format
    keywords = [element[0] for element in textrank_result]
    lemma_keywords = [lemmatizer.lemmatize(word_token_dict[keyword], pos='v') for keyword in keywords]
    ranks = [element[1] for element in textrank_result]

    textrank_df = pd.DataFrame()
    textrank_df['keyword'] = lemma_keywords; textrank_df['rank'] = ranks

    textrank_df.to_csv('./data' + save_path + filename, index=False)


if __name__ == '__main__':
    global data_path, save_path
    parser = argparse.ArgumentParser(description="-d input data path(csv) -s save path to store output")
    parser.add_argument('-d', help="input_data_path", required=True)
    parser.add_argument('-s', help="save_path", required=True)
    
    args = parser.parse_args()

    data_path = args.d; save_path = args.s
    print("data_path:", data_path)
    print("save_path:", save_path)
    print()

    textrank(data_path)