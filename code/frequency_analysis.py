import pandas as pd
import seaborn as sns

def frequency_analysis(word_token):
    #상위 30개까지만 확인
    frequency_series = pd.Series(word_token).value_counts().head(30)

    sns.set(rc={'figure.figsize': (30, 15)})
    splot = sns.barplot(y=frequency_series.index, x=frequency_series.values, orient='h')
    sfig = splot.get_figure()

    sfig.savefig('../figure/scuba_diving_safety.png')