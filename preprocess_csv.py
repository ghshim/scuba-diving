import pandas as pd

def remove_dup(df1_path, df2_path, dst_path, dst_name, column='title'):
    '''
    Concate two csv files and remove duplicate in the concatenated csv file.
    Then, store the result in csv format.

    Input:
        df1_path: path of the first csv file 
        df2_path: path of the second csv file 
        dst_path: destination path for saving the concatednated csv file
        dst_name: name for saving the concatednated csv file
        column: column to compare the duplicates
    Output:
        result_df: the result dataframe
    '''
    df1 = pd.read_csv(df1_path)
    df2 = pd.read_csv(df2_path)
    df = pd.concat([df1, df2], axis=0)
    result_df = df.drop_duplicates([column], keep='first')
    result_df.to_csv(dst_path + dst_name)

    return result_df

def extract_text(df):
    '''
    extract text(abstract) in data

    Input:
        data_path: path of csv file to extract texts
    Output:
        None
    '''
    texts = df['abstract'].to_list()
    return texts

