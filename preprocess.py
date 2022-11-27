import pandas as pd

def extract_text(data_path):
    '''
    extract text(abstract) in data
    '''
    df = pd.read_csv(data_path)
    texts = df['abstract'].to_list()
    return texts

def remove_dup():
    return