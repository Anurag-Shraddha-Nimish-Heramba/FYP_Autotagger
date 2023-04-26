import nltk
# nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import string

data = pd.read_csv('https://raw.githubusercontent.com/Anurag-Shraddha-Nimish-Heramba/FYP_Autotagger/master/mozilla_thunderbird.csv')
df = pd.DataFrame(data)

df = df.drop(['Priority', 'Duplicated_issue', 'Version', 'Created_time', 'Resolved_time', 'Resolution'], axis=1)


all_sentences = ""
all_sentences = df['Title'].str.cat(sep=' ')
all_sentences = all_sentences + (df['Description'].str.cat(sep=' '))

tokens = word_tokenize(all_sentences.lower())
# print(tokens)

stop_words = set(stopwords.words('english'))
tokens = [w for w in tokens if not w in stop_words and not w in set(map(str, string.punctuation))]
print(tokens[0:1000])