본 프로젝트는 스쿠버 다이빙 논문 동향 조사를 위함이며 주어진 논문에 대하여 텍스트 마이닝을 실시합니다. <br>
키워드 빈도수 분석, 텍스트랭크 분석을 실시하며 해당 결과를 바탕으로 빈도수 및 랭크 점수가 높은 Top 30개의 키워드를 추출하여 이를 t-SNE 그래프에 벡터로 표현합니다. <br>
또한, 토픽 모델링을 통해 논문 데이터에서 세부 주제를 뽑아내며, 각 세부 토픽의 분포를 확인합니다. <br>

## 코드 실행을 위해 필요한 Library
numpy <br>
pandas <br>
argparse <br>
matplotlib <br>
seaborn <br>
gensim <br>
nltk <br>

## 디렉토리 구조
<pre>
ㄴtextrank: TextRank를 적용하기 위해 필요한 라이브러리 
	출처: https://github.com/lovit/textrank/
  
ㄴdata: 크롤링을 통해 얻어진 파일 및 결과 데이터셋 폴더
    ㄴtopic2
      ㄴtrust_robot.csv: “trust” robot 키워드로 검색하여 얻은 크롤링 결과
      ㄴtopic2_YearCount.csv: 연도별 논문 개수 데이터셋
      ㄴtopic2_NewFrequency.csv: 단어 빈도수 분석 결과 데이터셋
      ㄴtopic2_TextRank.csv: TextRank 분석 결과 데이터셋
      ㄴtopic2_StemResult.csv: topic modeling에서 어근화 이전의 원본 단어 데이터셋
      ㄴtopic2_predicted.csv: topic modeling을 통해 분류된 논문의 topic 번호를 저장한 데이터셋
      ㄴtopic2_TopicCount.csv: 분류된 topic 별 논문의 개수를 저장한 데이터셋
    ㄴtopic3
      ㄴuser_experience.csv: “user” experience 키워드로 검색하여 얻은 크롤링 결과
      ㄴusability_wearable.csv: “usability” wearable 키워드로 검색하여 얻은 크롤링 결과
      ㄴuser*.csv: user_experience.csv와 usability_wearable.csv를 합하여 중복된 논문을 제거한 데이터셋
      그 외 나머지는 topic2와 동일합니다
    ㄴtopic6
      ㄴrisk_diving.csv: “risk” diving 키워드로 검색하여 얻은 크롤링 결과
      ㄴsafety_diving.csv: “safety” diving 키워드로 검색하여 얻은 크롤링 결과
      ㄴdiving*.csv: risk_diving.csv와 safety_diving.csv를 합하여 중복된 논문을 제거한 데이터셋
      그 외 나머지는 topic2와 동일합니다.

ㄴfigure: 결과 그래프 폴더
    ㄴtopic2
      ㄴtopic2_YearCount.png: 연도별 논문 개수를 시각화한 그래프
      ㄴtopic2_Frequency.png: Word Frequency Counter를 적용하여 빈도수가 높은 상위 30개의 단어의 빈도수를 시각화한 그래프
      ㄴtopic2_TextRank.png: TextRank를 적용하여 Rank 점수가 높은 상위 30개의 단어의 랭킹 점수를 시각화한 그래프
      ㄴtopic2_keyword_t-SNE.png: 논문 데이터셋에서 얻어진 모든 단어 토큰을 Word2Vector를 사용하여 벡터화한 후, 이를 t-SNE로 차원축소하여 2차원으로 나타낸 그래프. 
                                  단어는 Word Frequency Counter와 TextRank를 이용하여 얻어진 상위 30개의 키워드에 대해서만 그래프에 표시. 
                                  이를 통해 각 단어들의 관계(유사성 등)을 파악하기 위함.
                                  특히, Word Frequency Counter와 TextRank의 Top 30개의 키워드가 대부분 겹쳐, 이를 별도로 표시하였습니다. 
                                  아래의 그래프에서 초록색 점으로 표시된 단어는 Word Frequency Counter와 TextRank를 통해서 얻어진 키워들 중 공통된 키워드를 나타냈으며,
                                  파란색 +은 공통으로 선정된 단어 외의 TextRank로 선정된 단어, 빨간색 +은 공통으로 선정된 단어 외의 Word Frequency Counter로 선정된 단어를 표시합니다. 
      ㄴtopic2_topics_t-SNE.png:   논문을 Tf-idf Vecotrizer를 통해서 벡터화한 후 논문 별 세부 주제(topic)가 어디에 위치해있는지 
                                  t-SNE로 차원축소하여 2차원으로 표시한 그래프. Topic Modeling을 통해 분류된 세부 주제 사용하여 논문들 간의 관계(유사성 등)을 파악하기 위함.  
      ㄴtopic2_TopicModeling.html: Topic Modeling한 결과를 pyLDAvis 라이브러리를 통하여 시각화한 결과 (크롬 등과 같은 인터넷 브라우저로 열어야 합니다) 
        * Intertopic Distance Map(왼쪽): 주어진 키워드에 대한 논문 데이터들을 Topic Modeling을 통해 세부 주제로 분류했을 때, 분류된 논문들이 어디에 위치해있는지 PCA 차원 축소를 통해 나타낸 그래프
        * Top-10 Most Salient Terms(오른쪽): 각 세부 주제에서 빈도수가 높았던 상위 10개의 키워드들을 나타낸 그래프
      ㄴtopic2_TopicCount.png: 주어진 키워드에 대한 논문 데이터들을 Topic Modeling을 통해 세부 주제로 분류한 후, 각 세부 주제별 논문이 몇개 존재하는지 나타낸 그래프
   ㄴtopic3
      topic2와 동일합니다.
   ㄴtopic6
      topic2와 동일합니다.

preprocess_csv.py
year_count.py
apply_textrank.py
frequency_analysis.py
draw_plot.py
keword_t-SNE.py
topics_t-SNE.py
text_preprocessing.py
topic_count.py
topic.modeling.py
</pre>