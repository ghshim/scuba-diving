'''
데이터 정보
'''

def data_info(df, dir):
    '''
    전체 데이터의 개수와 데이터를 연도별로 분류하여 각 연도별 데이터의 개수를 dictionary로 리턴
    또한, 연도별 논문의 수를 csv로 변환 및 막대 그래프로 나타낸 후 dir folder에 저장 (x축: 연도, y축: 연도별 데이터 개수)
    
    input
      data: 전체 데이터

    output
      total_num: 전체 데이터 개수
      data_year: 연도를 key로 가지며 해당 년도의 데이터를 value로 가짐
    '''
    csv_name = "/DataInfo.csv"
    fig_name = "/DataInfo.png"
    csv_path = dir + csv_name; fig_path = dir + fig_name

    return total_num, data_year



def text2cv(data, dir, top_n):
    '''
    주어진 말뭉치를 Count Vector 변환 후 csv로 변환(전체 데이터) 후 저장
    및 top_n개에 대한 결과를 막대 그래프로 표현 후 저장 (x축: count, y축: word)
 
    input

    output
        countVec: text를 count vector로 변환한 전체 결과 (top_n X)
    '''
    csv_name = "/CountVector.csv"
    fig_name = "/CountVector.png"
    csv_path = dir + csv_name; fig_path = dir + fig_name
    return countVec



def text2rank(data, dir, top_n):
    '''
    주어진 말뭉치를 TextRank로 변환 후 csv로 변환(전체 데이터) 후 저장
    및 top_n개에 대한 결과를 막대 그래프로 표현 후 저장 (x축: textrank score, y축: word)

    input

    output
        textRank: text를 text rank로 변환한 결과
    '''
    csv_name = "/TextRank.csv"
    fig_name = "/TextRank.png"
    csv_path = dir + csv_name; fig_path = dir + fig_name

    return



def show_tSNE(data, dir, top_n):

    return



