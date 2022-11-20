from text_preprocessing import text_preprocessing
from scubaDiving.code.frequency_analysis import frequency_analysis

if __name__=="__main__":
    word_token = text_preprocessing()
    frequency_analysis(word_token)
