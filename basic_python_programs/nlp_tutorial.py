import sys
import nltk
print('Imported nltk ... ')
# nltk.download()
text_input_file = sys.argv[1].strip()

with open(text_input_file, 'r') as f:
    string_ = f.read()

import pandas as pd

df_keywords = pd.DataFrame({'keyword': ['Freedom', 'Freedom', 'Negro', 'Negro'],
                            'search_term': ['freedom', 'independence', 'negro', 'black']
                            })

sentences = nltk.sent_tokenize(string_)


df_each_sentence = pd.DataFrame()

text_part = []

for i in sentences:
    print(i)
    text_part.append(i)
df_each_sentence['sentence'] = text_part
print(df_each_sentence)


for i, row in df_each_sentence.iterrows():
    d = row['sentence']
    print(d)
    dict_ = {}
