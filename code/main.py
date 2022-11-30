from text_preprocessing import text_preprocessing
from frequency_analysis import frequency_analysis
from frequency_analysis import show_figure_forFrequency

from text_preprocessing import extract_texts
from frequency_analysis import tfidf_analysis
from frequency_analysis import show_figure_forTfidf



from convert_tsne import show_tsne
if __name__ == "__main__":
    #frequency_analysis
    data = extract_texts()
    word_token = text_preprocessing(data)
    frequency_obj = frequency_analysis(word_token)
    show_figure_forFrequency(frequency_obj)

    #tfidf_analysis
    #dataset = extract_texts()
    #tfidf_analysis(dataset)
    #show_figure_forTfidf(n, tfidf_obj)
