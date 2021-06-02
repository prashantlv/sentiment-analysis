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

emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace(',', '').replace("'", '').strip()
        #print(cleaned)    
        if ':' not in clear_line:
            print('BBBBBBBUUUUUUUUGGGGGGGGGG')
            pass
        else:
            words, emotions = clear_line.split(':')
            #print(words+':'+emotions)
            if words in corpora:
                emotion_list.append(emotions)

print(emotion_list)      

# from collections import Counter
# emotion_count = Counter(emotion_list)
# print(emotion_count[1])
