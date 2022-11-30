from setuptools import setup, find_packages
import textrank

setup(
    name=apply_textrank.__name__,
    version=apply_textrank.__version__,
    url='https://github.com/lovit/textrank/',
    author=apply_textrank.__author__,
    author_email='soy.lovit@gmail.com',
    description='TextRank based Summarizer (Keyword and key-sentence extractor)',
    packages=find_packages(),
    long_description=open('README.md', encoding="utf-8").read(),
    zip_safe=False,
    setup_requires=[]
)
