text = open('text.txt',encoding='utf-8').read()

#text preprocessing
text = text.lower()

import re
text = re.sub('[^a-zA-Z]',' ',text)
tokenized_text = text.split()

stopWords= open('stopwords.txt',encoding='utf-8').read()
stopWords=stopWords.lower().split()

corpora =[] 
for word in tokenized_text:
    if word not in stopWords:
        corpora.append(word)

print(corpora)
