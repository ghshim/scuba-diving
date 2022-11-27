from text_preprocessing import text_preprocessing
from frequency_analysis import frequency_analysis
from convert_tsne import show_tsne
if __name__ == "__main__":
    word_token = text_preprocessing()
    frequency_analysis(word_token)
    show_tsne()
