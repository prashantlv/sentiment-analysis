raw_text = open('text.txt',encoding='utf-8').read()

#text preprocessing

raw_text = raw_text.lower()

import re
text = re.sub('[^a-zA-Z]',' ',raw_text)
tokenized_text = text.split()

stopWords = open('stopwords.txt',encoding='utf-8').read()
stopWords = stopWords.lower().split()

final_text =[] 
for word in tokenized_text:
    if word not in stopWords:
        final_text.append(word)
#print(corpora)

emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace(',', '').replace("'", '').strip()
        #print(cleaned)    
        if ':' not in clear_line:
            print('Loooooooooooooooooooooooooke HERE !!!')
            pass
        else:
            words, emotions = clear_line.split(':')
            #print(words+':'+emotions)
            if words in final_text:
                emotion_list.append(emotions)

print(set(emotion_list))      

from collections import Counter
emotion_count = Counter(emotion_list)
print(emotion_count.most_common(2))

import matplotlib.pyplot as plt
plt.plot(emotion_count[0], emotion_count[1])
plt.show()




