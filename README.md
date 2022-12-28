# 코드 실행을 위해 필요한 Library
numpy <br>
pandas <br>
argparse <br>
matplotlib <br>
seaborn <br>
gensim <br>
nltk <br>

# 디렉토리 구조
ㄴtextrank: TextRank를 적용하기 위해 필요한 라이브러리 <br>
	출처: https://github.com/lovit/textrank/ <br> 
  <br>
ㄴdata: 크롤링을 통해 얻어진 파일 및 결과 데이터셋 폴더 <br>
    ㄴtopic2 <br>
      ㄴtrust_robot.csv: “trust” robot 키워드로 검색하여 얻은 크롤링 결과 <br>
      ㄴtopic2_YearCount.csv: 연도별 논문 개수 데이터셋 <br>
      ㄴtopic2_NewFrequency.csv: 단어 빈도수 분석 결과 데이터셋 <br>
      ㄴtopic2_TextRank.csv: TextRank 분석 결과 데이터셋 <br>
      ㄴtopic2_StemResult.csv: topic modeling에서 어근화 이전의 원본 단어 데이터셋 <br>
      ㄴtopic2_predicted.csv: topic modeling을 통해 분류된 논문의 topic 번호를 저장한 데이터셋 <br>
      ㄴtopic2_TopicCount.csv: 분류된 topic 별 논문의 개수를 저장한 데이터셋 <br>
    ㄴtopic3 <br>
      ㄴuser_experience.csv: “user” experience 키워드로 검색하여 얻은 크롤링 결과 <br>
      ㄴusability_wearable.csv: “usability” wearable 키워드로 검색하여 얻은 크롤링 결과 <br>
      ㄴuser*.csv: user_experience.csv와 usability_wearable.csv를 합하여 중복된 논문을 제거한 데이터셋 <br>
      그 외 나머지는 topic2와 동일합니다 <br>
    ㄴtopic6 <br>
      ㄴrisk_diving.csv: “risk” diving 키워드로 검색하여 얻은 크롤링 결과 <br>
      ㄴsafety_diving.csv: “safety” diving 키워드로 검색하여 얻은 크롤링 결과 <br>
      ㄴdiving*.csv: risk_diving.csv와 safety_diving.csv를 합하여 중복된 논문을 제거한 데이터셋 <br>
      그 외 나머지는 topic2와 동일합니다. <br>
 <br>
ㄴfigure: 결과 그래프 폴더 <br>
    ㄴtopic2 <br>
      ㄴtopic2_YearCount.png: 연도별 논문 개수를 시각화한 그래프 <br>
      ㄴtopic2_Frequency.png: Word Frequency Counter를 적용하여 빈도수가 높은 상위 30개의 단어의 빈도수를 시각화한 그래프 <br>
      ㄴtopic2_TextRank.png: TextRank를 적용하여 Rank 점수가 높은 상위 30개의 단어의 랭킹 점수를 시각화한 그래프 <br>
      ㄴtopic2_keyword_t-SNE.png: 논문 데이터셋에서 얻어진 모든 단어 토큰을 Word2Vector를 사용하여 벡터화한 후,  <br>이를 t-SNE로 차원축소하여 2차원으로 나타낸 그래프. 단어는 Word Frequency Counter와 TextRank를 이용하여 얻어진 상위 30개의 키워드에 대해서만 그래프에 표시. <br> 이를 통해 각 단어들의 관계(유사성 등)을 파악하기 위함. <br>
                                 특히, Word Frequency Counter와 TextRank의 Top 30개의 키워드가 대부분 겹쳐, 이를 별도로 표시하였습니다.  <br>아래의 그래프에서 초록색 점으로 표시된 단어는 Word Frequency Counter와 TextRank를 통해서 얻어진 키워들 중 공통된 키워드를 나타냈으며, 파란색 +은 공통으로 선정된 단어 외의 TextRank로 선정된 단어, 빨간색 +은 공통으로 선정된 단어 외의 Word Frequency Counter로 선정된 단어를 표시합니다.  <br>
      ㄴtopic2_topics_t-SNE.png: 논문을 Tf-idf Vecotrizer를 통해서 벡터화한 후 논문 별 세부 주제(topic)가 어디에 위치해있는지 t-SNE로 차원축소하여 2차원으로 표시한 그래프.  <br>Topic Modeling을 통해 분류된 세부 주제 사용하여 논문들 간의 관계(유사성 등)을 파악하기 위함.   <br>
      ㄴtopic2_TopicModeling.html: Topic Modeling한 결과를 pyLDAvis 라이브러리를 통하여 시각화한 결과 (크롬 등과 같은 인터넷 브라우저로 열어야 합니다)  <br>
        * Intertopic Distance Map(왼쪽): 주어진 키워드에 대한 논문 데이터들을 Topic Modeling을 통해 세부 주제로 분류했을 때, 분류된 논문들이 어디에 위치해있는지 PCA 차원 축소를 통해 나타낸 그래프 <br>
        * Top-10 Most Salient Terms(오른쪽): 각 세부 주제에서 빈도수가 높았던 상위 10개의 키워드들을 나타낸 그래프 <br>
      ㄴtopic2_TopicCount.png: 주어진 키워드에 대한 논문 데이터들을 Topic Modeling을 통해 세부 주제로 분류한 후, 각 세부 주제별 논문이 몇개 존재하는지 나타낸 그래프 <br>
   ㄴtopic3 <br>
      topic2와 동일합니다. <br>
   ㄴtopic6 <br>
      topic2와 동일합니다. <br>
 <br>
preprocess_csv.py <br>
year_count.py <br>
apply_textrank.py <br>
frequency_analysis.py <br>
draw_plot.py <br>
keword_t-SNE.py <br>
topics_t-SNE.py <br>
text_preprocessing.py <br>
topic_count.py <br>
topic.modeling.py <br>
