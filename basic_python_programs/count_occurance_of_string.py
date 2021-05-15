import json
from collections import Counter
import pandas as pd
df = pd.read_csv('file.csv')
print(df.shape)
d = df['COL_NAME'].to_list()
count_each = Counter(d)
final_dictionary = dict(count_each)
print(json.dumps(final_dictionary, indent=2))

with open('file.json', 'w') as f:
    f.write(json.dumps(final_dictionary, indent=2))

