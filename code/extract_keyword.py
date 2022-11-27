from gensim.summarization import keywords

text = ""

print(keywords(text, scores=True, lemmatize=True))